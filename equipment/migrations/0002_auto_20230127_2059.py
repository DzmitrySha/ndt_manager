# Generated by Django 3.2.13 on 2023-01-27 20:59

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('equipment', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='equipment',
            name='station_num',
            field=models.CharField(blank=True, max_length=2, verbose_name='Station number'),
        ),
        migrations.AlterField(
            model_name='equipment',
            name='start_op_date',
            field=models.DateField(blank=True, default=django.utils.timezone.now, verbose_name='Start operation date'),
        ),
    ]
