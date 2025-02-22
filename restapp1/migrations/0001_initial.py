# Generated by Django 5.1.5 on 2025-02-22 08:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('branch', models.CharField(max_length=5)),
                ('marks', models.IntegerField()),
                ('age', models.IntegerField()),
                ('date_created', models.DateTimeField()),
            ],
        ),
    ]
