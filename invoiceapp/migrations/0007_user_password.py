# Generated by Django 4.1.2 on 2022-10-14 06:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invoiceapp', '0006_admininfo_delete_note'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='password',
            field=models.TextField(null=True),
        ),
    ]
