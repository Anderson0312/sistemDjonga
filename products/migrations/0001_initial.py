# Generated by Django 5.0.4 on 2024-04-22 14:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('valor', models.EmailField(max_length=255)),
                ('description', models.CharField(max_length=255)),
                ('category', models.CharField(max_length=255)),
            ],
        ),
    ]