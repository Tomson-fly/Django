# Generated by Django 2.2 on 2021-07-21 07:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('house', '0005_auto_20210721_1132'),
    ]

    operations = [
        migrations.CreateModel(
            name='buyinfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('idcard', models.CharField(max_length=18)),
                ('phone', models.CharField(max_length=11)),
                ('money', models.IntegerField()),
                ('renttime', models.CharField(max_length=5)),
            ],
        ),
        # migrations.RemoveField(
        #     model_name='sec',
        #     name='built',
        # ),
        # migrations.RemoveField(
        #     model_name='sec',
        #     name='orientation',
        # ),
    ]
