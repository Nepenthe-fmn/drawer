# Generated by Django 3.0 on 2020-03-18 03:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0008_zan'),
    ]

    operations = [
        migrations.AlterField(
            model_name='zan',
            name='username',
            field=models.CharField(max_length=32, null=True),
        ),
    ]