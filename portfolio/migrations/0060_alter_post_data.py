# Generated by Django 4.0.4 on 2022-05-29 03:22

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0059_aptidao_tipo_alter_post_data'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='data',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 29, 4, 22, 35, 814545)),
        ),
    ]