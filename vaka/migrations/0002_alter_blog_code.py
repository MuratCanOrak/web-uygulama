# Generated by Django 3.2.6 on 2021-08-04 17:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vaka', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='code',
            field=models.CharField(editable=False, max_length=100, null=True, unique=True),
        ),
    ]
