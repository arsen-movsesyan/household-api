# Generated by Django 3.2 on 2023-09-13 21:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('passman', '0009_alter_account_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='recurringaccount',
            name='comment',
            field=models.TextField(null=True),
        ),
    ]
