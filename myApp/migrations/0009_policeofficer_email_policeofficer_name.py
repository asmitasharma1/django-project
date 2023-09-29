# Generated by Django 4.2.5 on 2023-09-23 05:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0008_remove_policeofficer_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='policeofficer',
            name='email',
            field=models.EmailField(default='user@gmail.com', max_length=254, unique=True),
        ),
        migrations.AddField(
            model_name='policeofficer',
            name='name',
            field=models.CharField(default='', max_length=100),
        ),
    ]