# Generated by Django 4.0.6 on 2022-12-14 14:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Material',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('inv_number', models.CharField(db_index=True, max_length=12, verbose_name='Инвентарный номер')),
                ('name', models.CharField(db_index=True, max_length=100, verbose_name='Наименование МЦ')),
                ('count', models.PositiveIntegerField(default=0, verbose_name='Количество')),
            ],
            options={
                'verbose_name': 'Матценность',
                'verbose_name_plural': 'Матценности',
            },
        ),
        migrations.AlterModelOptions(
            name='location',
            options={'ordering': ['place'], 'verbose_name': 'Расположение', 'verbose_name_plural': 'Расположение'},
        ),
        migrations.AlterField(
            model_name='location',
            name='place',
            field=models.CharField(db_index=True, max_length=50, verbose_name='Расположение МЦ'),
        ),
    ]
