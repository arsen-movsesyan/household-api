# Generated by Django 3.2 on 2021-05-04 14:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('passman', '0005_alter_address_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='address',
            options={'ordering': ['period_start']},
        ),
    ]
