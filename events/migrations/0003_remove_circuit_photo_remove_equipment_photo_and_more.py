# Generated by Django 4.2.13 on 2024-06-10 18:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0002_category_equipment_kart_circuit_booking'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='circuit',
            name='photo',
        ),
        migrations.RemoveField(
            model_name='equipment',
            name='photo',
        ),
        migrations.RemoveField(
            model_name='kart',
            name='photo',
        ),
    ]
