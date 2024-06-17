from django.db.models import TextChoices
from django.utils.translation import gettext_lazy as _


class SocialNetworkChannelChoices(TextChoices):
    GITHUB = "github", _("Github")
    INSTAGRAM = "instagram", _("Instagram")
    YOUTUBE = "youtube", _("Youtube")
    FACEBOOK = "facebook", _("Facebook")
    LINKEDIN = "linkedin", _("Linkedin")
    WHATSAPP = "whatsapp", _("Whatsapp")
    X = "x", _("X")
    TWITCH = "twitch", _("Twitch")
