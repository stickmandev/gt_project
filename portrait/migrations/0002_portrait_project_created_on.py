# Generated by Django 3.0.5 on 2020-09-11 07:13

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('portrait', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='portrait_project',
            name='created_on',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
