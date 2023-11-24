# Generated by Django 4.2.7 on 2023-11-19 22:36

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Articulo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=150)),
                ('subtitulo', models.CharField(max_length=250)),
                ('contenido', ckeditor.fields.RichTextField()),
                ('autor', models.CharField(max_length=150)),
                ('creado', models.DateTimeField(auto_now_add=True)),
                ('editado', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
