# Generated by Django 4.2.6 on 2023-10-22 15:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lecturer', '0002_userimage_lecture_lecturer_lecture_qr'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lecture',
            name='end_date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='lecture',
            name='end_time',
            field=models.TimeField(),
        ),
        migrations.AlterField(
            model_name='lecture',
            name='start_date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='lecture',
            name='start_time',
            field=models.TimeField(),
        ),
    ]
