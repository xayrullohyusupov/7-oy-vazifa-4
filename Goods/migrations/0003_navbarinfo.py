# Generated by Django 5.1b1 on 2024-07-24 13:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Goods', '0002_category_description_category_is_active'),
    ]

    operations = [
        migrations.CreateModel(
            name='NavbarInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
                ('phone', models.CharField(blank=True, max_length=15, null=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
            ],
        ),
    ]
