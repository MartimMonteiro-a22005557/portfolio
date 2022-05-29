# Generated by Django 4.0.4 on 2022-05-28 04:45

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0042_alter_post_data_alter_post_imagem'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='data',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 28, 5, 45, 31, 57873)),
        ),
        migrations.AlterField(
            model_name='post',
            name='imagem',
            field=models.ImageField(upload_to='./portfolio/media/images/'),
        ),
    ]
