# Generated by Django 4.2.9 on 2024-06-15 18:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_alter_socialnetwork_unique_together'),
    ]

    operations = [
        migrations.CreateModel(
            name='AccountLink',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Atualizado em')),
                ('title', models.CharField(max_length=25, verbose_name='Título')),
                ('url', models.URLField(verbose_name='URL')),
                ('account', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Usuário')),
            ],
            options={
                'verbose_name': 'Link do usuário',
                'verbose_name_plural': 'Links do usuário',
                'unique_together': {('title', 'url', 'account')},
            },
        ),
    ]
