# Generated by Django 4.0.4 on 2022-04-12 18:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movie_api', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Contact',
            new_name='Movie',
        ),
    ]
