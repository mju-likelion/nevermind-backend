# Generated by Django 3.1 on 2020-10-03 11:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subscription', '0004_auto_20201003_0019'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='app_name',
            field=models.CharField(max_length=512),
        ),
    ]
