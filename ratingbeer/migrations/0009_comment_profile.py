# Generated by Django 4.1.1 on 2022-10-12 14:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ratingbeer', '0008_remove_comment_avatar_remove_comment_rang_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='profile',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='ratingbeer.profile'),
        ),
    ]
