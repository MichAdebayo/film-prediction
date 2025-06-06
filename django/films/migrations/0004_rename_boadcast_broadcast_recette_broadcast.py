# Generated by Django 5.2 on 2025-04-23 12:24

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('films', '0003_boadcast_remove_movie_room_recette'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Boadcast',
            new_name='Broadcast',
        ),
        migrations.AddField(
            model_name='recette',
            name='broadcast',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='recettes', to='films.broadcast'),
        ),
    ]
