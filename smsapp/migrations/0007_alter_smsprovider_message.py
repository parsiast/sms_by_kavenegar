# Generated by Django 5.1.1 on 2024-09-07 13:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('smsapp', '0006_alter_smsprovider_message'),
    ]

    operations = [
        migrations.AlterField(
            model_name='smsprovider',
            name='message',
            field=models.TextField(),
        ),
    ]