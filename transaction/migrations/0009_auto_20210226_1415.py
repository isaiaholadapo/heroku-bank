# Generated by Django 3.1.7 on 2021-02-26 13:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('transaction', '0008_auto_20210226_1404'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='AccountDetails',
            new_name='AccountDetail',
        ),
        migrations.DeleteModel(
            name='Interest',
        ),
    ]
