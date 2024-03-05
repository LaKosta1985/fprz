# Generated by Django 5.0.1 on 2024-02-29 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_alter_user_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='status_in_Feder',
            field=models.CharField(blank=True, choices=[('true', 'член федерации'), ('false', 'не состоит')], null=True, verbose_name='Член Федерации?'),
        ),
    ]