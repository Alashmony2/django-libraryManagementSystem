# Generated by Django 4.2.3 on 2023-08-23 09:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lms_app', '0004_rename_cost_book_rental_cost'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=7, null=True),
        ),
    ]
