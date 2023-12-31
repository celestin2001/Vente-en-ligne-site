# Generated by Django 4.1.2 on 2023-12-26 21:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gestionproduits', '0009_card'),
    ]

    operations = [
        migrations.CreateModel(
            name='CartItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField()),
                ('cart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestionproduits.card')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestionproduits.produits')),
            ],
        ),
    ]