# Generated by Django 3.1.6 on 2021-04-23 22:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mjapp', '0004_auto_20210423_1740'),
    ]

    operations = [
        migrations.AlterField(
            model_name='serviceoffered',
            name='service',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='mjapp.services', verbose_name='Service offered'),
        ),
    ]
