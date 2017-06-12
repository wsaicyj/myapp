# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-05-11 14:36
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('description', models.TextField()),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='photos')),
                ('caption', models.CharField(blank=True, max_length=250)),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='PhotoGallery.Item')),
            ],
            options={
                'ordering': ['title'],
            },
        ),
    ]
