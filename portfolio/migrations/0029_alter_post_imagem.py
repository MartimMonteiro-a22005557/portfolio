# Generated by Django 4.0.4 on 2022-05-28 03:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0028_alter_post_data'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='imagem',
            field=models.FileField(upload_to='.'),
        ),
    ]