# Generated by Django 3.2.8 on 2021-11-03 16:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20211103_0522'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='pic',
            field=models.ImageField(upload_to='usr/%y'),
        ),
    ]
