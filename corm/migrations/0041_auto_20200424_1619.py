# Generated by Django 3.0.4 on 2020-04-24 16:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('corm', '0040_auto_20200424_1613'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='contribution',
            options={'ordering': ('-timestamp',), 'verbose_name_plural': 'Contributions'},
        ),
    ]
