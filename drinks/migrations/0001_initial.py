# Generated by Django 4.0.3 on 2022-05-11 06:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Drink',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=15)),
                ('type', models.CharField(max_length=7)),
                ('company', models.CharField(max_length=16)),
                ('desc', models.CharField(max_length=100)),
            ],
        ),
    ]
