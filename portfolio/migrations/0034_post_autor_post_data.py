# Generated by Django 4.0.4 on 2022-05-28 04:20

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0033_alter_post_imagem'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='autor',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='data',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 28, 5, 20, 19, 943313)),
        ),
    ]