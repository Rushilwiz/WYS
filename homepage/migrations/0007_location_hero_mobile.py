# Generated by Django 3.1 on 2020-08-26 19:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0006_auto_20200826_1858'),
    ]

    operations = [
        migrations.AddField(
            model_name='location',
            name='hero_mobile',
            field=models.ImageField(default='hero-mobile.png', upload_to='heros'),
        ),
    ]
