# Generated by Django 4.2.4 on 2023-09-05 09:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_transaction'),
    ]

    operations = [
        migrations.RenameField(
            model_name='transaction',
            old_name='purchased',
            new_name='purchased_quan',
        ),
    ]
