# Generated by Django 4.2.5 on 2023-09-19 12:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='people',
            name='age',
            field=models.IntegerField(blank=True, default=None, null=True, verbose_name='Возраст'),
        ),
    ]