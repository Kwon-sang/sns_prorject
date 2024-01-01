# Generated by Django 4.2 on 2024-01-01 21:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='profile_image',
            field=models.ImageField(blank=True, upload_to='accounts/profile/%Y/%m/%d'),
        ),
        migrations.AlterField(
            model_name='user',
            name='website_url',
            field=models.URLField(blank=True),
        ),
    ]
