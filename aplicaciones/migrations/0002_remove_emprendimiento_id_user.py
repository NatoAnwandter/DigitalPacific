# Generated by Django 4.1.3 on 2022-11-23 18:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('aplicaciones', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='emprendimiento',
            name='id_user',
        ),
    ]
