# Generated by Django 2.2.14 on 2021-08-15 17:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0016_orderitem_invited_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='invited_date',
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='invited_date',
            field=models.DateTimeField(),
        ),
    ]
