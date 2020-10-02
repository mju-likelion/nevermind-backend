# Generated by Django 3.1 on 2020-10-02 21:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subscription', '0002_auto_20200930_0017'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subscription',
            name='sub_type',
            field=models.CharField(choices=[('W', 'week'), ('M', 'month'), ('Y', 'year'), ('L', 'life_time')], default='M', max_length=2),
        ),
    ]
