# Generated by Django 3.1.6 on 2021-05-15 09:36

import Item.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Item', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='image',
            field=Item.fields.ThumbnailImageField(upload_to='photos'),
        ),
    ]