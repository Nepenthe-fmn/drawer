# Generated by Django 3.0 on 2020-03-29 05:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0016_auto_20200329_1037'),
    ]

    operations = [
        migrations.RenameField(
            model_name='news',
            old_name='userSend',
            new_name='userInfoSend',
        ),
    ]