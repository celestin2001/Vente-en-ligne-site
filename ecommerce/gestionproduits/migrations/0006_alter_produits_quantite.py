# Generated by Django 5.0.3 on 2024-03-20 13:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestionproduits', '0005_alter_commande_date_commande'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produits',
            name='quantite',
            field=models.IntegerField(null=True),
        ),
    ]
