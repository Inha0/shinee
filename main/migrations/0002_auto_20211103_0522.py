# Generated by Django 3.2.8 on 2021-11-03 05:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='album',
        ),
        migrations.RemoveField(
            model_name='user',
            name='point',
        ),
    ]