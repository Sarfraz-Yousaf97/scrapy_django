# Generated by Django 4.1.2 on 2023-02-10 12:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_imagemodel_trademarkmodel'),
    ]

    operations = [
        migrations.AddField(
            model_name='freepatent',
            name='file',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
