# Generated by Django 2.1.2 on 2019-08-09 19:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('realtors', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='realtor',
            name='photo',
            field=models.ImageField(upload_to='media/photos/%Y/%m/%d/'),
        ),
    ]
