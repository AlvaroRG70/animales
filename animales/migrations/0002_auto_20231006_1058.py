# Generated by Django 3.2.22 on 2023-10-06 08:58

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('animales', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Animals',
            new_name='Animal',
        ),
        migrations.RenameModel(
            old_name='colaboradores',
            new_name='Colaborador',
        ),
        migrations.RenameModel(
            old_name='Protectoras',
            new_name='Protectora',
        ),
    ]
