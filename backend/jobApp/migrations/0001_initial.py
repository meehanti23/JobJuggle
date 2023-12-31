# Generated by Django 4.2.4 on 2023-08-29 16:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='JobApp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company', models.CharField(max_length=100)),
                ('position', models.CharField(max_length=100)),
                ('url', models.TextField()),
                ('date_applied', models.DateField()),
                ('status', models.CharField(max_length=100)),
                ('notes', models.TextField()),
            ],
        ),
    ]
