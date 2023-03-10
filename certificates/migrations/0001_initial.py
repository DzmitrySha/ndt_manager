# Generated by Django 4.1.5 on 2023-02-05 19:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Certificate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(max_length=16)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Created date')),
                ('start_date', models.DateField(default=django.utils.timezone.now, verbose_name='Start date')),
                ('finish_date', models.DateField(default=django.utils.timezone.now, verbose_name='Finish date')),
                ('level', models.IntegerField(choices=[(2, 2), (3, 3)], default=2, verbose_name='Report type')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
