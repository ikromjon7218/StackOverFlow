# Generated by Django 4.2 on 2023-04-19 12:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('asosiy', '0004_rename_ism_savol_matn'),
    ]

    operations = [
        migrations.AlterField(
            model_name='savol',
            name='sana',
            field=models.DateField(auto_now_add=True),
        ),
    ]
