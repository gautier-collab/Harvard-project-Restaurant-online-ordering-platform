# Generated by Django 3.0.3 on 2020-07-20 02:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='cart_version',
            field=models.FloatField(default=0, null=True),
        ),
    ]
