# Generated by Django 4.0.2 on 2023-12-09 16:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='genre',
            old_name='genre',
            new_name='name',
        ),
    ]
