# Generated by Django 4.2.7 on 2023-11-25 20:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EventList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('eventName', models.CharField(max_length=100)),
                ('eventDate', models.CharField(max_length=100)),
                ('eventTime', models.CharField(max_length=100)),
                ('eventURL', models.CharField(max_length=100)),
            ],
        ),
    ]