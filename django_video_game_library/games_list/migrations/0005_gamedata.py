# Generated by Django 5.1.1 on 2024-12-06 09:02

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('games_list', '0004_remove_game_rating_remove_game_review'),
    ]

    operations = [
        migrations.CreateModel(
            name='GameData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_free', models.BooleanField()),
                ('detailed_description', models.TextField()),
                ('short_description', models.TextField()),
                ('header_image', models.URLField()),
                ('appid', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='games_list.game')),
            ],
        ),
    ]
