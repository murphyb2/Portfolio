# Generated by Django 2.1.1 on 2018-10-06 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PortfolioApp', '0013_auto_20181006_1005'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='height',
            field=models.PositiveIntegerField(blank=True, default=0, editable=False, null=True),
        ),
        migrations.AlterField(
            model_name='image',
            name='width',
            field=models.PositiveIntegerField(blank=True, default=0, editable=False, null=True),
        ),
    ]
