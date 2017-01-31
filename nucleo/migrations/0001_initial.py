# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-28 03:21
from __future__ import unicode_literals

import autoslug.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Expo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('expo', models.CharField(blank=True, max_length=255, unique=True)),
                ('slug', autoslug.fields.AutoSlugField(editable=False, populate_from='expo', unique=True)),
                ('fechaInaugura', models.DateField()),
                ('fechaClausura', models.DateField()),
                ('textoCur', models.TextField(max_length=1500)),
                ('imagen', models.FileField(blank=True, upload_to='license')),
                ('sala', models.CharField(blank=True, choices=[('SALA1', 'Sala 1'), ('SALA2', 'Sala 2'), ('SALA3', 'Sala 3'), ('SALA4', 'Sala 4'), ('SALA5', 'Sala 5'), ('SALA6', 'Sala 6'), ('SALA7', 'Sala 7'), ('SALA8', 'Sala 8'), ('SALA9', 'Sala 9')], max_length=20)),
            ],
            options={
                'verbose_name': 'Exposición',
                'ordering': ['-fechaInaugura'],
                'verbose_name_plural': 'Exposiciones',
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag', models.CharField(max_length=50, unique=True)),
                ('slug', autoslug.fields.AutoSlugField(editable=False, populate_from='tag')),
            ],
            options={
                'ordering': ['tag'],
            },
        ),
        migrations.AddField(
            model_name='expo',
            name='tag',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='nucleo.Tag'),
        ),
    ]