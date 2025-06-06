# Generated by Django 5.1.4 on 2025-05-16 08:50

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomerAddress',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mobile_number', models.CharField(max_length=10, validators=[django.core.validators.RegexValidator(message='Mobile number must be exactly 10 digits.', regex='^\\d{10}$')])),
            ],
        ),
        migrations.CreateModel(
            name='profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('address', models.TextField()),
                ('city', models.CharField(max_length=100)),
                ('pincode', models.IntegerField(blank=True, null=True)),
                ('country', models.CharField(max_length=100)),
                ('mobile_number', models.CharField(blank=True, max_length=10, null=True, validators=[django.core.validators.RegexValidator(message='Mobile number must be exactly 10 digits.', regex='^\\d{10}$')])),
                ('alternate_mobile', models.CharField(blank=True, max_length=10, null=True, validators=[django.core.validators.RegexValidator(message='Mobile number must be exactly 10 digits.', regex='^\\d{10}$')])),
            ],
        ),
    ]
