# Generated by Django 5.1.1 on 2024-09-07 12:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('smsapp', '0005_alter_smsprovider_options_alter_smsprovider_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='smsprovider',
            name='message',
            field=models.TextField(default='blankedone'),
        ),
    ]
