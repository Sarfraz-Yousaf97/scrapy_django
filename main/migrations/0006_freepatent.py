# Generated by Django 4.1.2 on 2023-02-04 10:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_alter_quote_related_link'),
    ]

    operations = [
        migrations.CreateModel(
            name='FreePatent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=500, null=True)),
                ('description', models.CharField(blank=True, max_length=2000, null=True)),
            ],
        ),
    ]
