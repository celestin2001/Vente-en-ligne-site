# Generated by Django 4.1.2 on 2023-12-26 16:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gestionproduits', '0007_alter_cart_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='produit',
        ),
        migrations.RemoveField(
            model_name='order',
            name='user',
        ),
        migrations.DeleteModel(
            name='Cart',
        ),
        migrations.DeleteModel(
            name='Order',
        ),
    ]