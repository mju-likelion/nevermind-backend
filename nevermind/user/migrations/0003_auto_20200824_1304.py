# Generated by Django 3.1 on 2020-08-24 13:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_session'),
    ]

    operations = [
        migrations.AlterField(
            model_name='session',
            name='email',
            field=models.ForeignKey(db_column='email', on_delete=django.db.models.deletion.CASCADE, to='user.user'),
        ),
    ]
