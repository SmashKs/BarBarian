# Generated by Django 2.1.3 on 2018-11-13 03:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
                name='News',
                fields=[
                    ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                    ('author', models.CharField(blank=True, max_length=64, null=True)),
                    ('title', models.CharField(max_length=128, unique=True)),
                    ('country', models.CharField(blank=True, max_length=2)),
                    ('description', models.CharField(blank=True, max_length=512, null=True)),
                    ('url', models.CharField(blank=True, max_length=256, null=True)),
                    ('urlToImage', models.CharField(blank=True, max_length=256, null=True)),
                    ('published_at', models.DateTimeField()),
                    ('content', models.CharField(blank=True, max_length=1024, null=True)),
                    ('created_at', models.DateTimeField(auto_now_add=True)),
                    ('updated_at', models.DateTimeField(auto_now=True)),
                ],
                options={
                    'db_table': 'newses',
                },
        ),
        migrations.CreateModel(
                name='Source',
                fields=[
                    ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                    ('s_id', models.CharField(blank=True, max_length=128, null=True)),
                    ('name', models.CharField(blank=True, max_length=128, null=True)),
                    ('created_at', models.DateTimeField(auto_now_add=True)),
                    ('updated_at', models.DateTimeField(auto_now=True)),
                ],
                options={
                    'db_table': 'news_sources',
                },
        ),
        migrations.CreateModel(
                name='Subscriber',
                fields=[
                    ('token', models.CharField(max_length=128, primary_key=True, serialize=False)),
                    ('firebase_token', models.CharField(max_length=128, unique=True)),
                    ('keywords', models.CharField(max_length=512, null=True)),
                    ('created_at', models.DateTimeField(auto_now_add=True)),
                    ('updated_at', models.DateTimeField(auto_now=True)),
                ],
                options={
                    'db_table': 'subscribers',
                },
        ),
        migrations.AlterUniqueTogether(
                name='news',
                unique_together={('id', 'title')},
        ),
    ]
