# Generated by Django 4.1.5 on 2023-02-18 20:07

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('equipment', '0009_alter_equipment_equipment_type'),
        ('stations', '0004_alter_station_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Created date')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated date')),
                ('report_num', models.CharField(default='01-2023', max_length=10, unique=True, verbose_name='Report number')),
                ('report_date', models.DateField(default=django.utils.timezone.now, verbose_name='Report date')),
                ('report_type', models.CharField(choices=[('NDT', 'NDT'), ('TD', 'TD')], default='NDT', max_length=12, verbose_name='Report type')),
                ('parts_names', models.CharField(blank=True, max_length=120, verbose_name='Parts names')),
                ('description', models.TextField(blank=True, verbose_name='Description')),
                ('equipment', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='equipment', to='equipment.equipment', verbose_name='Equipment')),
                ('station', models.ForeignKey(blank=True, default=1, on_delete=django.db.models.deletion.PROTECT, to='stations.station', verbose_name='Station')),
            ],
        ),
    ]
