# Generated by Django 3.2.3 on 2021-05-27 07:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='profile/defaultIMG.gif', upload_to='profile'),
        ),
    ]
