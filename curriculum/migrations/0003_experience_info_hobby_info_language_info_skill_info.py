# Generated by Django 5.0.6 on 2024-06-30 15:46

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('curriculum', '0002_formation_info'),
    ]

    operations = [
        migrations.AddField(
            model_name='experience',
            name='info',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='experience_info', to='curriculum.info'),
        ),
        migrations.AddField(
            model_name='hobby',
            name='info',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='hobby_info', to='curriculum.info'),
        ),
        migrations.AddField(
            model_name='language',
            name='info',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='language_info', to='curriculum.info'),
        ),
        migrations.AddField(
            model_name='skill',
            name='info',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='skill_info', to='curriculum.info'),
        ),
    ]
