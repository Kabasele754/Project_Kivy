# Generated by Django 4.1 on 2022-08-07 02:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chatApp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='friend',
            name='profile',
        ),
        migrations.AddField(
            model_name='friend',
            name='name',
            field=models.CharField(default='achille', max_length=100),
            preserve_default=False,
        ),
    ]