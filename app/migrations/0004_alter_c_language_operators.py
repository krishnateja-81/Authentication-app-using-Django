# Generated by Django 4.2.4 on 2023-09-28 03:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_rename_jaav_language_java_language_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='c_language',
            name='operators',
            field=models.PositiveIntegerField(default=0, verbose_name='operators'),
        ),
    ]
