# Generated by Django 5.1 on 2024-08-14 14:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='model',
            name='age',
            field=models.IntegerField(default=''),
        ),
        migrations.AlterField(
            model_name='model',
            name='name',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='model',
            name='place',
            field=models.CharField(default='', max_length=200),
        ),
    ]
