# Generated by Django 3.1.4 on 2021-01-28 08:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_order_restourant'),
    ]

    operations = [
        migrations.CreateModel(
            name='FastFoodMenu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('price', models.CharField(max_length=80)),
                ('image', models.ImageField(upload_to='myapp/images/')),
            ],
        ),
    ]
