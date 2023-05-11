# Generated by Django 4.1.7 on 2023-05-01 15:12

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=8)),
                ('capacity', models.IntegerField(validators=[django.core.validators.MinValueValidator(1)])),
                ('location', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client_name', models.CharField(max_length=100)),
                ('client_email', models.EmailField(max_length=254)),
                ('client_phone', models.CharField(max_length=20)),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('party_size', models.IntegerField(validators=[django.core.validators.MinValueValidator(1)])),
                ('total_amount', models.DecimalField(decimal_places=2, max_digits=8)),
                ('cancellation_policy', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ReservationConfirmation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('confirmation_number', models.CharField(max_length=50)),
                ('confirmation_date', models.DateTimeField(auto_now_add=True)),
                ('reservation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='camping.reservation')),
            ],
        ),
        migrations.CreateModel(
            name='ImageObjet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name="Titre de l'image")),
                ('image', models.ImageField(upload_to='event/')),
                ('caption', models.TextField(blank=True, null=True, verbose_name='Caption')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('object', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='camping.event', verbose_name='Objet')),
            ],
            options={
                'verbose_name': 'Image',
                'verbose_name_plural': 'Images',
            },
        ),
    ]
