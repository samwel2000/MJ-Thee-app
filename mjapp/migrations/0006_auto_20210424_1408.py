# Generated by Django 3.1.6 on 2021-04-24 19:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mjapp', '0005_auto_20210423_1743'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='serviceoffered',
            name='service',
        ),
        migrations.AddField(
            model_name='serviceoffered',
            name='service',
            field=models.ManyToManyField(to='mjapp.Services', verbose_name='Service offered'),
        ),
    ]
