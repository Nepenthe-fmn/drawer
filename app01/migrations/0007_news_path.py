# Generated by Django 3.0 on 2020-03-15 10:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0006_auto_20200312_1105'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='path',
            field=models.CharField(max_length=128, null=True),
        ),
    ]