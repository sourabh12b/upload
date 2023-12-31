# Generated by Django 4.2.4 on 2023-08-31 14:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='earbud',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('image', models.ImageField(upload_to='Downloads')),
                ('price', models.FloatField()),
                ('quantity', models.IntegerField()),
                ('available', models.BooleanField(default=True)),
                ('desc', models.TextField()),
            ],
        ),
    ]
