# Generated by Django 3.2.5 on 2021-08-26 14:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0003_auto_20210826_1431'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='orginal_bag',
            new_name='original_bag',
        ),
    ]
