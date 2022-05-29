# Generated by Django 4.0.4 on 2022-05-29 00:24

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0053_tecnologia_acronimo_tecnologia_ano_de_criacao_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='data',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 29, 1, 24, 27, 652015)),
        ),
        migrations.AlterField(
            model_name='projeto',
            name='linguagem',
            field=models.ManyToManyField(blank=True, related_name='linguagens', to='portfolio.linguagem'),
        ),
    ]
