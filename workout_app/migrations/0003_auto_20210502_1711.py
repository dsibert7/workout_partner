# Generated by Django 2.2 on 2021-05-03 00:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workout_app', '0002_auto_20210502_1657'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='gender',
            field=models.CharField(choices=[('male', 'Male'), ('female', 'Female')], max_length=1, null=True),
        ),
    ]