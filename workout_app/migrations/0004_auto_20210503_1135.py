# Generated by Django 2.2 on 2021-05-03 18:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workout_app', '0003_auto_20210502_1711'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='gender',
            field=models.BooleanField(choices=[('true', 'Male'), ('false', 'Female')], max_length=1, null=True),
        ),
    ]