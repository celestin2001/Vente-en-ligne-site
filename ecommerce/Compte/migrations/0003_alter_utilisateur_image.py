# Generated by Django 5.0.3 on 2024-03-15 03:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Compte', '0002_alter_utilisateur_first_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='utilisateur',
            name='image',
            field=models.ImageField(blank=True, upload_to='image'),
        ),
    ]
