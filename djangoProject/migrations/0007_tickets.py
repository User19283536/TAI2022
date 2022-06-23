# Generated by Django 3.2.5 on 2022-05-22 16:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djangoProject', '0006_bookings_email'),
    ]

    operations = [
        migrations.CreateModel(
            name='tickets',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('type', models.CharField(max_length=50)),
                ('price', models.FloatField(default=19.9)),
            ],
        ),
    ]