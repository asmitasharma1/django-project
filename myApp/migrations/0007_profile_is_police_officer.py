# Generated by Django 4.2.5 on 2023-09-22 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0006_policeofficer'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='is_police_officer',
            field=models.BooleanField(default=False),
        ),
    ]