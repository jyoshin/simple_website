# Generated by Django 4.1 on 2022-08-07 09:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='item',
            old_name='compplete',
            new_name='complete',
        ),
    ]
