# Generated by Django 4.2.5 on 2023-09-20 16:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0004_rename_user_profile_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='User',
            new_name='user',
        ),
    ]
