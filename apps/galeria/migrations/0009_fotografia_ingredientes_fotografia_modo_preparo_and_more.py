# Generated by Django 5.0.4 on 2024-04-25 17:40

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('galeria', '0008_alter_fotografia_data_fotografia_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='fotografia',
            name='ingredientes',
            field=models.TextField(default='', max_length=15000),
        ),
        migrations.AddField(
            model_name='fotografia',
            name='modo_preparo',
            field=models.TextField(default='', max_length=15000),
        ),
        migrations.AlterField(
            model_name='fotografia',
            name='data_fotografia',
            field=models.DateTimeField(default=datetime.datetime(2024, 4, 25, 14, 40, 33, 190869)),
        ),
    ]
