# Generated by Django 3.2.6 on 2021-08-05 06:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vaka', '0003_alter_blog_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='link',
            field=models.URLField(max_length=250),
        ),
    ]
