# Generated by Django 3.0.6 on 2020-05-27 15:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='bith_date',
            new_name='birth_date',
        ),
    ]
