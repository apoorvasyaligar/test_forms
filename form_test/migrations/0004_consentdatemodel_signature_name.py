# Generated by Django 3.2.7 on 2021-09-03 04:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('form_test', '0003_auto_20210902_2046'),
    ]

    operations = [
        migrations.AddField(
            model_name='consentdatemodel',
            name='signature_name',
            field=models.CharField(default='yourname', max_length=100),
        ),
    ]
