import re
import uuid

from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils.translation import gettext_lazy as _
from django.core import validators

from apps.core.managers import AccountManager
from apps.core.choices import SocialNetworkChannelChoices


class BaseModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("Criado em"))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_("Atualizado em"))

    class Meta:
        abstract = True


class Account(BaseModel, AbstractBaseUser, PermissionsMixin):
    username = models.CharField(
        _("Nome de usuário"),
        max_length=15,
        unique=True,
        help_text=_(
            "Obrigatório. Máximo de 15 caracteres. Letras, números e caracteres @/./+/-/_ permitidos."
        ),
        validators=[
            validators.RegexValidator(
                re.compile("^[\w.@+-]+$"),
                _("Insira um nome de usuário válido."),
                "invalid",
            )
        ],
    )
    first_name = models.CharField(_("Nome"), max_length=30, null=True, blank=True)
    last_name = models.CharField(_("Sobrenome"), max_length=30, null=True, blank=True)
    email = models.EmailField(_("E-mail"), max_length=255, unique=True)
    email_is_confirmed = models.BooleanField(
        _("E-mail está confirmado"),
        default=False,
        help_text=_("Designa se este usuário confirmou seu e-mail."),
    )
    is_staff = models.BooleanField(
        _("É Staff?"),
        default=False,
        help_text=_(
            "Designa se o usuário pode efetuar login neste site de administração."
        ),
    )

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["email"]

    objects = AccountManager()

    class Meta:
        verbose_name = _("Usuário")
        verbose_name_plural = _("Usuários")

    def __str__(self) -> str:
        return self.get_username_display()

    @property
    def full_name(self):
        full_name = f"{self.first_name or ''} {self.last_name or ''}"

        if full_name.strip() == "":
            return self.username

        return full_name.strip()

    def get_all_socialnetworks(self):
        return self.socialnetwork_set.all()

    def get_all_accountlinks(self):
        return self.accountlink_set.all().order_by("updated_at")

    def get_profile_avatar_url(self):
        if hasattr(self, "profile") and self.profile.avatar:
            return self.profile.avatar.url
        return "https://placehold.co/112x111"

    def get_username_display(self):
        return f"@{self.username}"


class Profile(BaseModel):
    account = models.OneToOneField(
        Account,
        verbose_name=_("Usuário"),
        on_delete=models.CASCADE
    )
    avatar = models.ImageField(
        verbose_name=_("Avatar"),
        upload_to="profile/avatars",
        null=True, blank=True
    )

    class Meta:
        verbose_name = _("Perfil")
        verbose_name_plural = _("Perfis")

    def __str__(self) -> str:
        return self.account.full_name


class SocialNetwork(BaseModel):
    account = models.ForeignKey(
        Account,
        blank=True,
        verbose_name=_("Usuário"),
        on_delete=models.CASCADE
    )
    channel = models.CharField(
        verbose_name=_("Canal"),
        max_length=20,
        choices=SocialNetworkChannelChoices.choices
    )
    url = models.URLField(
        verbose_name=_("URL"),
    )

    class Meta:
        verbose_name = _("Rede social")
        verbose_name_plural = _("Redes sociais")
        unique_together = ["account", "channel"]

    def __str__(self) -> str:
        return f"{self.account.username}/{self.channel}"

    def get_channel(self):
        return "twitter" if self.channel == "x" else self.channel


class AccountLink(BaseModel):
    account = models.ForeignKey(
        Account,
        blank=True,
        verbose_name=_("Usuário"),
        on_delete=models.CASCADE
    )
    title = models.CharField(
        verbose_name=_("Título"),
        max_length=25
    )
    url = models.URLField(
        verbose_name=_("URL"),
    )

    class Meta:
        verbose_name = _("Link do usuário")
        verbose_name_plural = _("Links do usuário")
        unique_together = ["title", "url", "account"]

    def __str__(self) -> str:
        return f"{self.account.username}/{self.title}"
