# Generated by Django 2.2 on 2021-07-21 03:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('house', '0004_auto_20210720_1600'),
    ]

    operations = [
        # migrations.RemoveField(
        #     model_name='sec',
        #     name='built',
        # ),
        # migrations.RemoveField(
        #     model_name='sec',
        #     name='orientation',
        # ),
        migrations.AddField(
            model_name='new',
            name='location',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='rent',
            name='location',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='sec',
            name='location',
            field=models.CharField(max_length=10, null=True),
        ),
    ]