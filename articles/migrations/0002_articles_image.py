# Generated by Django 4.1 on 2022-08-27 12:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='articles',
            name='image',
            field=models.ImageField(blank=True, default='default.jpg', upload_to=''),
        ),
    ]