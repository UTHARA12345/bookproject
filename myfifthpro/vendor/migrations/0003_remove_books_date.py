# Generated by Django 3.0.6 on 2020-06-25 17:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vendor', '0002_auto_20200624_1217'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='books',
            name='date',
        ),
    ]