# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-10-13 19:37
from __future__ import unicode_literals

from django.db import migrations, models
import portailva.utils.validators


class Migration(migrations.Migration):

    dependencies = [
        ('association', '0018_auto_20171013_1858'),
    ]

    operations = [
        migrations.AlterField(
            model_name='association',
            name='logo_url',
            field=models.URLField(blank=True, help_text="Privilégiez les liens en HTTPS. Assurez-vous que le lien que vous fournissez pointe directement sur l'image (pas de page d'affichage comme Google Drive ou autres) et que l'image soit accessible.", validators=[portailva.utils.validators.validate_image_url], verbose_name='URL du logo'),
        ),
    ]
