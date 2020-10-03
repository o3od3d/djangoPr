# Generated by Django 3.1 on 2020-10-03 12:11

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lob', '0006_delete_food'),
    ]

    operations = [
        migrations.CreateModel(
            name='Food',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('food_name', models.CharField(max_length=100)),
                ('food_recodeDate', models.DateTimeField(auto_now_add=True)),
                ('food_expirationDate', models.DateTimeField(default=datetime.timezone)),
                ('food_info', models.IntegerField()),
                ('food_remainDate', models.DateTimeField(default=datetime.timezone)),
                ('food_img', models.ImageField(blank=True, null=True, upload_to='images/')),
            ],
        ),
    ]