# Generated by Django 4.1.5 on 2023-02-13 20:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='post',
            field=models.CharField(default='', max_length=48),
        ),
    ]
