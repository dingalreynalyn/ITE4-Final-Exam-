# Generated by Django 4.1.5 on 2023-01-11 07:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stat', models.CharField(max_length=5)),
                ('score', models.IntegerField()),
                ('outoff', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='UserSelection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('selection', models.CharField(max_length=100)),
            ],
        ),
    ]
