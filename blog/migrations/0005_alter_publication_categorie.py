# Generated by Django 4.2.16 on 2024-11-16 08:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_categorie_publication_categorie'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publication',
            name='categorie',
            field=models.ForeignKey(default='default', on_delete=django.db.models.deletion.CASCADE, to='blog.categorie'),
        ),
    ]