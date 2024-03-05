# Generated by Django 5.0.1 on 2024-03-01 07:15

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_remove_new_img_body_new_img_body_1_new_img_body_2_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Table_Record',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Таблица рекорда')),
                ('gender', models.CharField(choices=[('мужской', 'мужской'), ('женский', 'женский')], max_length=100, verbose_name='Пол')),
                ('equipment', models.CharField(choices=[('классика', 'классика'), ('экипировка', 'экипировка')], max_length=100, verbose_name='Экипировка')),
                ('Competition', models.CharField(choices=[('троеборье', 'троеборье'), ('жим', 'жим')], max_length=100, verbose_name='Упражнение')),
            ],
            options={
                'verbose_name': 'Добавление\\редактирование таблицы рекорда',
                'verbose_name_plural': 'Добавление\\редактирование таблицы рекорда',
                'db_table': 'record',
            },
        ),
        migrations.AlterModelOptions(
            name='table_cat',
            options={'verbose_name': 'Категория норматива', 'verbose_name_plural': 'Категория норматива'},
        ),
        migrations.CreateModel(
            name='Table_Cat_Record',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(choices=[('53', '53'), ('59', '59'), ('66', '66'), ('74', '74'), ('83', '83'), ('93', '93'), ('105', '105'), ('120', '120'), ('120+', '120+'), ('43', '43'), ('47', '47'), ('52', '52'), ('57', '57'), ('63', '63'), ('69', '69'), ('76', '76'), ('84', '84'), ('84+', '84+')], max_length=100, verbose_name='Категории')),
                ('squat_name', models.CharField(blank=True, max_length=100, null=True, verbose_name='Имя рекордсмена в приседе')),
                ('squat', models.FloatField(blank=True, max_length=100, null=True, verbose_name='Приседание, кг')),
                ('date_squat', models.DateField(blank=True, null=True, verbose_name='Дата рекорда в приседании')),
                ('place_squat', models.CharField(blank=True, max_length=100, null=True, verbose_name='Место рекорда в приседании')),
                ('press_name', models.CharField(max_length=100, verbose_name='Имя рекордсмена в жиме')),
                ('press', models.FloatField(max_length=100, verbose_name='Жим, кг')),
                ('date_press', models.DateField(blank=True, null=True, verbose_name='Дата рекорда в жиме')),
                ('place_press', models.CharField(max_length=100, verbose_name='Место рекорда в жиме')),
                ('lift_name', models.CharField(blank=True, max_length=100, null=True, verbose_name='Имя рекордсмена в тяге')),
                ('lift', models.FloatField(blank=True, max_length=100, null=True, verbose_name='Тяга, кг')),
                ('date_lift', models.DateField(blank=True, null=True, verbose_name='Дата рекорда в тяге')),
                ('place_lift', models.CharField(blank=True, max_length=100, null=True, verbose_name='Место рекорда в тяге')),
                ('sum_name', models.CharField(blank=True, max_length=100, null=True, verbose_name='Имя рекордсмена в сумме')),
                ('sum', models.FloatField(blank=True, max_length=100, null=True, verbose_name='Сумма, кг')),
                ('date_sum', models.DateField(blank=True, null=True, verbose_name='Дата рекорда в сумме')),
                ('place_sum', models.CharField(blank=True, max_length=100, null=True, verbose_name='Место рекорда, сумма')),
                ('cut_rec', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main.table_record')),
            ],
            options={
                'verbose_name': 'Добавление\\редактирование рекорда',
                'verbose_name_plural': 'Добавление\\редактирование рекорда',
                'db_table': 'cut_rec',
            },
        ),
    ]
