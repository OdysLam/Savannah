# Generated by Django 3.0.4 on 2020-06-11 15:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('corm', '0058_auto_20200611_1450'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contribution',
            name='location',
            field=models.URLField(blank=True, max_length=512, null=True),
        ),
    ]
