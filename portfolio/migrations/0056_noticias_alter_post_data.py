# Generated by Django 4.0.4 on 2022-05-29 02:35

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0055_alter_post_data'),
    ]

    operations = [
        migrations.CreateModel(
            name='Noticias',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('descricao', models.CharField(max_length=50)),
                ('link', models.URLField(blank=True)),
            ],
        ),
        migrations.AlterField(
            model_name='post',
            name='data',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 29, 3, 35, 38, 795220)),
        ),
    ]