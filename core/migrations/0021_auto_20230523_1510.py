# Generated by Django 3.1.3 on 2023-05-23 12:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0020_auto_20230523_1503'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='pickup_address',
            field=models.CharField(blank=True, help_text='Размер', max_length=255, verbose_name='Размер'),
        ),
    ]