# Generated by Django 3.2.2 on 2021-05-14 04:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('schooltracker', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='school',
            new_name='School',
        ),
    ]
