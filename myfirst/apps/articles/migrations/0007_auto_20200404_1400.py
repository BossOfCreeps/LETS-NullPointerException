# Generated by Django 3.0.4 on 2020-04-04 07:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0006_auto_20200404_1327'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invite',
            name='event',
            field=models.IntegerField(),
        ),
    ]