# Generated by Django 2.0b1 on 2019-06-25 20:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0008_auto_20190625_2117'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gameslocation',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='gameslocation',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]