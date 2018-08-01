# Generated by Django 2.0.7 on 2018-08-01 09:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Actor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('actor_name', models.CharField(max_length=100)),
                ('pub_date', models.DateTimeField(auto_now_add=True, verbose_name='date published')),
                ('date_of_birth', models.DateField()),
                ('nationality', models.CharField(max_length=100)),
                ('up_votes', models.IntegerField(default=0)),
                ('actor_image', models.ImageField(upload_to='actor_image')),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('movie_title', models.CharField(max_length=300)),
                ('pub_date', models.DateTimeField(auto_now_add=True, verbose_name='date published')),
                ('date_of_movie', models.DateField()),
                ('language', models.CharField(max_length=100)),
                ('movie_type', models.CharField(max_length=100)),
                ('movie_image', models.ImageField(upload_to='movie_image')),
            ],
        ),
        migrations.AddField(
            model_name='actor',
            name='movie',
            field=models.ManyToManyField(to='movies.Movie'),
        ),
    ]