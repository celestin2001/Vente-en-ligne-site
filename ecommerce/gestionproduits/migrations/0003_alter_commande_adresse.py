# Generated by Django 5.0.3 on 2024-03-18 03:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestionproduits', '0002_commande'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commande',
            name='adresse',
            field=models.CharField(max_length=30, null=True),
        ),
    ]