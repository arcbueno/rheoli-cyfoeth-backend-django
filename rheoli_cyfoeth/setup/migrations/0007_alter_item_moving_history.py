# Generated by Django 5.0.4 on 2024-04-30 01:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('setup', '0006_rename_department_id_item_department_movinghistory_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='moving_history',
            field=models.ManyToManyField(blank=True, null=True, to='setup.movinghistory'),
        ),
    ]