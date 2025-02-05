# Generated by Django 2.2 on 2021-07-20 02:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='new',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.IntegerField()),
                ('type', models.CharField(max_length=10)),
                ('area', models.FloatField()),
                ('community', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='rent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('joint', models.BinaryField()),
                ('price', models.IntegerField()),
                ('type', models.CharField(max_length=10)),
                ('area', models.FloatField()),
                ('orientation', models.CharField(max_length=10)),
                ('community', models.CharField(max_length=50)),
                ('metro', models.BinaryField()),
                ('heating', models.BinaryField()),
                ('decoration', models.BinaryField()),
                ('showing', models.BinaryField()),
            ],
        ),
        migrations.CreateModel(
            name='sec',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.IntegerField()),
                ('type', models.CharField(max_length=10)),
                ('area', models.FloatField()),
                ('orientation', models.CharField(max_length=10)),
                ('community', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='user',
            fields=[
                ('name', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('password', models.CharField(max_length=30)),
            ],
        ),
    ]
