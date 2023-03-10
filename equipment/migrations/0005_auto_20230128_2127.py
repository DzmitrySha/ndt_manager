# Generated by Django 3.2.13 on 2023-01-28 21:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('equiptypes', '0001_initial'),
        ('stations', '0003_alter_station_address'),
        ('equipment', '0004_auto_20230128_2126'),
    ]

    operations = [
        migrations.AlterField(
            model_name='equipment',
            name='equipment_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='equiptypes', to='equiptypes.equiptype', verbose_name='Equipment type'),
        ),
        migrations.AlterField(
            model_name='equipment',
            name='station',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='stations', to='stations.station', verbose_name='Station'),
        ),
    ]
