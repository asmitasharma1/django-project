# Generated by Django 4.2.5 on 2023-09-20 15:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0002_profile'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='User',
            new_name='user',
        ),
    ]
