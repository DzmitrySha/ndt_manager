# Generated by Django 4.1.5 on 2023-01-31 18:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('equipment', '0007_alter_equipment_last_repair_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='equipment',
            name='name',
            field=models.CharField(max_length=120, unique=True, verbose_name='Name/model'),
        ),
        migrations.AlterField(
            model_name='equipment',
            name='register_num',
            field=models.CharField(blank=True, max_length=16, unique=True, verbose_name='Registration number'),
        ),
    ]
