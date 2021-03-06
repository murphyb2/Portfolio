# Generated by Django 2.0.8 on 2018-12-18 22:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('picture', models.ImageField(height_field='height', null=True, upload_to='pictures/%Y/%m/%d/', width_field='width')),
                ('alt_text', models.CharField(max_length=200, null=True)),
                ('width', models.PositiveIntegerField(blank=True, default=0, editable=False, null=True)),
                ('height', models.PositiveIntegerField(blank=True, default=0, editable=False, null=True)),
                ('portfolio_section', models.CharField(choices=[('home', 'Home'), ('colorFilm', '35mm Color'), ('bwFilm', '35mm BW'), ('music', 'Music'), ('prof_pic', 'Profile Picture')], max_length=100)),
                ('priority', models.IntegerField()),
                ('is_showcase_image', models.BooleanField(default=False)),
            ],
        ),
        migrations.AddField(
            model_name='about',
            name='prof_pic',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='PortfolioApp.Image'),
        ),
    ]
