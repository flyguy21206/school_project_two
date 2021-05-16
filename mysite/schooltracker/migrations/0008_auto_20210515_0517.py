# Generated by Django 3.2.2 on 2021-05-15 09:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('schooltracker', '0007_auto_20210515_0403'),
    ]

    operations = [
        migrations.AlterField(
            model_name='department',
            name='faculty',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='schooltracker.faculty'),
        ),
        migrations.AlterField(
            model_name='student',
            name='Certificate_Type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='schooltracker.certificate_type'),
        ),
        migrations.AlterField(
            model_name='student',
            name='department',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='schooltracker.department'),
        ),
        migrations.AlterField(
            model_name='student',
            name='grade',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='schooltracker.grade'),
        ),
        migrations.AlterField(
            model_name='student',
            name='school',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='schooltracker.school'),
        ),
    ]