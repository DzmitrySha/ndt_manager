# Generated by Django 4.1.5 on 2023-02-17 20:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_user_post'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='post',
            field=models.CharField(default='', max_length=48, verbose_name='Post'),
        ),
    ]
