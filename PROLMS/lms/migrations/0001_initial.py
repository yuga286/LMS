# Generated by Django 5.0.6 on 2024-06-05 15:03

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Info',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('First_Name', models.CharField(max_length=100)),
                ('Middle_Name', models.CharField(max_length=100)),
                ('Last_Name', models.CharField(max_length=100)),
                ('User_Name', models.CharField(max_length=100)),
                ('Contact_Number', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'Student_Data',
            },
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('Book_ID', models.AutoField(primary_key=True, serialize=False)),
                ('Book_Name', models.CharField(max_length=256)),
                ('Book_Image', models.ImageField(upload_to='lmss/')),
                ('Book_Count', models.IntegerField()),
                ('Publication_Year', models.DateTimeField(blank=True, null=True)),
                ('Publisher', models.CharField(blank=True, max_length=100)),
                ('author', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='lms.author')),
            ],
            options={
                'db_table': 'Book_Data',
            },
        ),
    ]
