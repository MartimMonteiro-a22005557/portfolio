# Generated by Django 4.0.4 on 2022-05-27 00:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0008_remove_cadeira_professores_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cadeira',
            old_name='professoresDasPraticas',
            new_name='professoresPraticas',
        ),
    ]
