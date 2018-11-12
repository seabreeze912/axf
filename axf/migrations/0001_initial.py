# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-11-09 01:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FoodTypes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('typeid', models.CharField(max_length=200)),
                ('typename', models.CharField(max_length=200)),
                ('childtypenames', models.CharField(max_length=200)),
                ('typesort', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Goods',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('productid', models.CharField(max_length=200)),
                ('productimg', models.CharField(max_length=200)),
                ('productname', models.CharField(max_length=200)),
                ('productlongname', models.CharField(max_length=200)),
                ('isxf', models.NullBooleanField(default=False)),
                ('pmdesc', models.CharField(max_length=200)),
                ('specifics', models.CharField(max_length=200)),
                ('price', models.CharField(max_length=200)),
                ('marketprice', models.CharField(max_length=200)),
                ('categoryid', models.CharField(max_length=200)),
                ('childcid', models.CharField(max_length=200)),
                ('childcidname', models.CharField(max_length=200)),
                ('dealerid', models.CharField(max_length=200)),
                ('storenums', models.IntegerField()),
                ('productnum', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Mustbuy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.CharField(max_length=200)),
                ('name', models.CharField(max_length=30)),
                ('trackid', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Nav',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.CharField(max_length=200)),
                ('name', models.CharField(max_length=30)),
                ('trackid', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Shop',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.CharField(max_length=200)),
                ('name', models.CharField(max_length=30)),
                ('trackid', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Wheel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.CharField(max_length=200)),
                ('name', models.CharField(max_length=30)),
                ('trackid', models.CharField(max_length=30)),
            ],
        ),
    ]