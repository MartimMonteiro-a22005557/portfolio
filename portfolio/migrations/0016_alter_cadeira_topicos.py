# Generated by Django 4.0.4 on 2022-05-27 03:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0015_alter_cadeira_professorespraticas_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cadeira',
            name='topicos',
            field=models.TextField(blank=True, null=True),
        ),
    ]