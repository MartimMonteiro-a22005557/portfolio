# Generated by Django 4.0.4 on 2022-05-27 22:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0021_alter_cadeira_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cadeira',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='pessoa',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
