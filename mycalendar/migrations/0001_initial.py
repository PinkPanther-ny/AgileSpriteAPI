# Generated by Django 3.2.8 on 2021-12-25 15:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(default='null', max_length=256)),
                ('user_id', models.CharField(default='null', max_length=256)),
                ('location', models.CharField(default='null', max_length=256)),
                ('start_time', models.DateTimeField()),
                ('end_time', models.DateTimeField()),
                ('related_people', models.CharField(default='null', max_length=256)),
                ('date', models.DateField()),
                ('comments', models.TextField()),
                ('category', models.CharField(default='null', max_length=256)),
            ],
        ),
    ]
