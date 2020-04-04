# Generated by Django 3.0.4 on 2020-04-04 03:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0003_event_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='name',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='event',
            name='picture',
            field=models.URLField(default='https://hh.ru/employer-logo/3184173.png'),
        ),
        migrations.AlterField(
            model_name='event',
            name='text',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='event',
            name='time',
            field=models.DateTimeField(),
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=500)),
                ('text', models.TextField()),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='articles.Event')),
            ],
        ),
    ]