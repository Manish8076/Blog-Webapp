# Generated by Django 4.2.4 on 2023-08-03 12:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pro1', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='allblog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=122)),
                ('author', models.CharField(max_length=90)),
                ('posted_date', models.DateField(auto_now_add=True)),
                ('content', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='popularblog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=122)),
                ('author', models.CharField(max_length=90)),
                ('posted_date', models.DateField(auto_now_add=True)),
                ('content', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
