# Generated by Django 2.1 on 2018-09-22 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PortfolioApp', '0006_auto_20180921_1048'),
    ]

    operations = [
        migrations.AddField(
            model_name='home',
            name='title',
            field=models.CharField(default='Home', max_length=100),
        ),
        migrations.AlterField(
            model_name='image',
            name='alt_text',
            field=models.CharField(max_length=200, null=True),
        ),
    ]