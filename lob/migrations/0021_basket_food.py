# Generated by Django 3.1 on 2020-10-06 08:48

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lob', '0020_auto_20201006_1745'),
    ]

    operations = [
        migrations.CreateModel(
            name='Basket',
            fields=[
                ('basket_id', models.AutoField(primary_key=True, serialize=False)),
                ('basket_contents', models.TextField()),
                ('basket_reservationTime', models.TimeField()),
                ('basket_info', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Food',
            fields=[
                ('food_id', models.AutoField(primary_key=True, serialize=False)),
                ('food_name', models.CharField(max_length=100)),
                ('food_recodeDate', models.DateTimeField(auto_now_add=True)),
                ('food_expirationDate', models.DateTimeField(default=datetime.timezone)),
                ('food_info', models.IntegerField(null=True)),
                ('food_remainDate', models.IntegerField(null=True)),
                ('food_img', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('user_email', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lob.user')),
            ],
        ),
    ]