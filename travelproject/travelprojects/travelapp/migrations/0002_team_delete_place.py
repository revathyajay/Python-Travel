# Generated by Django 4.1.5 on 2023-01-11 05:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travelapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('teamname', models.CharField(max_length=250)),
                ('teamimage', models.ImageField(upload_to='photos')),
                ('teamdesc', models.TextField()),
            ],
        ),
        migrations.DeleteModel(
            name='Place',
        ),
    ]
