# Generated by Django 3.1 on 2020-08-28 21:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_auto_20200824_2322'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='pwd',
            field=models.CharField(max_length=80),
        ),
    ]