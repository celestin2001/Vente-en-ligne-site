# Generated by Django 5.0.3 on 2024-03-21 06:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestionproduits', '0002_alter_produits_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produits',
            name='image',
            field=models.ImageField(upload_to='media'),
        ),
    ]
