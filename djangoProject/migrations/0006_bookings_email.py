# Generated by Django 3.2.5 on 2022-05-22 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djangoProject', '0005_bookings'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookings',
            name='email',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
