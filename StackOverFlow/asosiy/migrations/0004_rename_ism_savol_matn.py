# Generated by Django 4.2 on 2023-04-19 12:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('asosiy', '0003_izoh'),
    ]

    operations = [
        migrations.RenameField(
            model_name='savol',
            old_name='ism',
            new_name='matn',
        ),
    ]