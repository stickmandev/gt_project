# Generated by Django 3.0.5 on 2020-09-25 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0031_auto_20200922_2025'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='post',
            new_name='blog_post',
        ),
        migrations.AlterField(
            model_name='blog_post',
            name='categories',
            field=models.ManyToManyField(related_name='post', to='blog.Category'),
        ),
    ]
