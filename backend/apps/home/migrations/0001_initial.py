# Generated by Django 3.2.4 on 2021-10-22 21:16

import cloudinary.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('tags', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Home',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.IntegerField(db_index=True, verbose_name='Price')),
                ('rent_price', models.IntegerField(db_index=True, verbose_name='Rent')),
                ('main_image', cloudinary.models.CloudinaryField(blank=True, max_length=255, null=True, verbose_name='Main_image')),
                ('sub_image1', cloudinary.models.CloudinaryField(blank=True, max_length=255, null=True, verbose_name='Sub_image1')),
                ('sub_image2', cloudinary.models.CloudinaryField(blank=True, max_length=255, null=True, verbose_name='Sub_image2')),
                ('sub_image3', cloudinary.models.CloudinaryField(blank=True, max_length=255, null=True, verbose_name='Sub_image3')),
                ('sub_image4', cloudinary.models.CloudinaryField(blank=True, max_length=255, null=True, verbose_name='Sub_image4')),
                ('state', models.CharField(db_index=True, default='State', max_length=30, verbose_name='State')),
                ('address', models.CharField(db_index=True, default='Address', max_length=100, verbose_name='Address')),
                ('layout', models.CharField(db_index=True, default='BHK', max_length=30, verbose_name='Layout')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created Datetime')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated Datetime')),
                ('tag', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tags.tag')),
            ],
            options={
                'db_table': 'home',
            },
        ),
    ]
