# Generated by Django 3.0.4 on 2020-04-22 17:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('corm', '0037_auto_20200420_0254'),
    ]

    operations = [
        migrations.AlterField(
            model_name='conversation',
            name='content',
            field=models.TextField(blank=True, null=True),
        ),
    ]
