# Generated by Django 3.2.25 on 2024-12-28 05:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(max_length=30)),
                ('YearOfRelease', models.DateField(blank=True)),
                ('Genre', models.CharField(max_length=30)),
                ('IMDBRating', models.FloatField(blank=True, null=True)),
                ('Plot', models.CharField(max_length=30)),
                ('Cast', models.CharField(max_length=30)),
                ('Director', models.CharField(max_length=30)),
                ('Runtime', models.FloatField(blank=True, null=True)),
                ('Language', models.CharField(blank=True, choices=[('hindi', 'Hindi'), ('tamil', 'Tamil'), ('malayalam', 'Malayalam'), ('english', 'English')], max_length=45)),
            ],
        ),
    ]
