# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-12-20 05:50
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ImageAttributes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img_type', models.CharField(max_length=128, null=True)),
                ('color', models.CharField(max_length=128, null=True)),
                ('variant', models.CharField(max_length=128, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ImageModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('images_field', models.BinaryField()),
            ],
        ),
        migrations.AddField(
            model_name='imageattributes',
            name='image',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='images.ImageModel'),
        ),
    ]
