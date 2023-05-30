# Generated by Django 4.2.1 on 2023-05-30 14:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Auto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('placa', models.CharField(max_length=17, unique=True)),
                ('marca', models.CharField(max_length=100)),
                ('color', models.CharField(max_length=50)),
                ('año', models.PositiveIntegerField()),
                ('foto', models.ImageField(upload_to='autos')),
                ('kilometraje', models.PositiveIntegerField()),
                ('modelo', models.CharField(max_length=100)),
                ('trim', models.CharField(max_length=100)),
                ('estado', models.CharField(max_length=50)),
            ],
        ),
    ]
