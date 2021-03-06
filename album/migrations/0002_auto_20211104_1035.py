# Generated by Django 3.2.8 on 2021-11-04 10:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('album', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, unique=True)),
            ],
        ),
        migrations.AddField(
            model_name='album',
            name='category',
            field=models.CharField(blank=True, max_length=30, null=True, verbose_name='Category'),
        ),
        migrations.AlterField(
            model_name='album',
            name='album_subname',
            field=models.CharField(max_length=100),
        ),
    ]
