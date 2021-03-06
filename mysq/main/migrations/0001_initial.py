# Generated by Django 3.2.5 on 2021-07-12 19:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dots',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('x_value', models.FloatField(max_length=15, verbose_name='X')),
                ('y_value', models.FloatField(max_length=15, verbose_name='Y')),
                ('r_value', models.IntegerField(max_length=3, verbose_name='R')),
                ('result', models.BooleanField(verbose_name='Result')),
            ],
            options={
                'verbose_name': 'Точка',
                'verbose_name_plural': 'Точки',
            },
        ),
    ]
