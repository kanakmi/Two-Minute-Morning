# Generated by Django 3.2 on 2021-07-17 13:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0009_bill_creator'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bill',
            name='paid',
        ),
    ]
