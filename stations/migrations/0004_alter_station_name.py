# Generated by Django 4.1.5 on 2023-01-31 18:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stations', '0003_alter_station_address'),
    ]

    operations = [
        migrations.AlterField(
            model_name='station',
            name='name',
            field=models.CharField(max_length=60, unique=True, verbose_name='Name'),
        ),
    ]
