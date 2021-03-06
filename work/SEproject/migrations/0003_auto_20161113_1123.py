# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2016-11-13 03:23
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('SEproject', '0002_auto_20161107_1619'),
    ]

    operations = [
        migrations.CreateModel(
            name='user',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=15)),
                ('email', models.EmailField(default='blank@qq.com', max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='userdata',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(max_length=200)),
                ('title', models.CharField(max_length=200)),
                ('time', models.DateTimeField()),
                ('date', models.TextField()),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SEproject.user')),
            ],
        ),
        migrations.DeleteModel(
            name='testhtml',
        ),
    ]
