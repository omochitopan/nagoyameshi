# Generated by Django 5.0.7 on 2024-08-02 06:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nagoyameshi', '0002_specialholiday'),
    ]

    operations = [
        migrations.AddField(
            model_name='restaurant',
            name='specialholiday',
            field=models.ManyToManyField(blank=True, to='nagoyameshi.specialholiday', verbose_name='定休日'),
        ),
    ]
