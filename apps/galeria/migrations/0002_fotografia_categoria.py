# Generated by Django 5.0.4 on 2024-04-25 03:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('galeria', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='fotografia',
            name='categoria',
            field=models.CharField(choices=[('Economicas', 'Econômicas'), ('Japonesa', 'Japonesa'), ('Doces', 'Doces'), ('Lanches', 'Lanches'), ('Italiana', 'Italiana')], default='', max_length=100),
        ),
    ]