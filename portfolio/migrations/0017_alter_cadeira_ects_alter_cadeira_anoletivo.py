# Generated by Django 4.0.4 on 2022-05-27 03:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0016_alter_cadeira_topicos'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cadeira',
            name='ECTS',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='cadeira',
            name='anoletivo',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]