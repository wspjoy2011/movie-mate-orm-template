# Generated by Django 4.2.6 on 2024-11-11 22:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0003_alter_movie_gross_alter_movie_imdb_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='moviedirector',
            name='collaboration_years',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='moviedirector',
            name='comments',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='moviedirector',
            name='role',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='moviegenre',
            name='added_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='moviegenre',
            name='importance_level',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='moviegenre',
            name='notes',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='moviestar',
            name='character_name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='moviestar',
            name='debut',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='moviestar',
            name='role',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='moviestar',
            name='salary',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AddField(
            model_name='moviestar',
            name='screen_time',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
