# Generated by Django 4.2.5 on 2023-11-25 05:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0013_complaint_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='MissingPerson',
            fields=[
                ('complaint', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='myApp.complaint')),
                ('missing_person_name', models.CharField(blank=True, max_length=255, null=True)),
                ('missing_person_description', models.TextField(blank=True, null=True)),
                ('missing_person_photo', models.ImageField(blank=True, null=True, upload_to='missing_person_photos/')),
            ],
        ),
    ]
