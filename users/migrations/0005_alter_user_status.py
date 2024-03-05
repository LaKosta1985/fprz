# Generated by Django 5.0.1 on 2024-03-01 08:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_user_status_in_feder'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='status',
            field=models.CharField(blank=True, choices=[('admin', 'admin'), ('prezident', 'prezident'), ('secret', 'secret'), ('antidoping', 'antidoping'), ('free', 'free')], default='free', null=True, verbose_name='Статус'),
        ),
    ]
