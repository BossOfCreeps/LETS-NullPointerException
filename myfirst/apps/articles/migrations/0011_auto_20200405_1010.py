# Generated by Django 3.0.4 on 2020-04-05 03:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0010_chat_chatid'),
    ]

    operations = [
        migrations.AddField(
            model_name='chat',
            name='chat_id',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='chat',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
