# Generated by Django 3.0.4 on 2020-04-20 02:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('corm', '0036_auto_20200417_1629'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='date_added',
            field=models.DateTimeField(db_index=True),
        ),
    ]