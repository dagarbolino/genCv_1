# Generated by Django 5.0.6 on 2024-07-09 18:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('curriculum', '0004_remove_experience_date_experience_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='experience',
            name='end_date_of_experience',
            field=models.DateField(blank=True, null=True, verbose_name="date de fin de l'expérience"),
        ),
        migrations.AlterField(
            model_name='experience',
            name='start_date_of_experience',
            field=models.DateField(blank=True, null=True, verbose_name="date de début de l'expérience"),
        ),
        migrations.AlterField(
            model_name='formation',
            name='end_date_of_formation',
            field=models.DateField(blank=True, null=True, verbose_name='date de fin de la formation'),
        ),
        migrations.AlterField(
            model_name='formation',
            name='start_date_of_formation',
            field=models.DateField(blank=True, null=True, verbose_name='date de début de la formation'),
        ),
    ]
