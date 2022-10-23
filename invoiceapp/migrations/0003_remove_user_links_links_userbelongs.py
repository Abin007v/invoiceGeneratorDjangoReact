# Generated by Django 4.1.2 on 2022-10-11 16:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('invoiceapp', '0002_links_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='links',
        ),
        migrations.AddField(
            model_name='links',
            name='userBelongs',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='invoiceapp.user'),
        ),
    ]
