# Generated by Django 5.1 on 2024-09-22 18:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_links'),
    ]

    operations = [
        migrations.RenameField(
            model_name='links',
            old_name='user',
            new_name='applicant',
        ),
    ]
