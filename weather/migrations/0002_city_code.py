# Generated by Django 3.2.5 on 2021-07-21 14:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('weather', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='city',
            name='code',
            field=models.CharField(default=0, max_length=25),
        ),
    ]
