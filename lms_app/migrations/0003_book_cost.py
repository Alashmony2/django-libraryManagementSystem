# Generated by Django 4.2.3 on 2023-08-22 17:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lms_app', '0002_rename_books_book'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='cost',
            field=models.DecimalField(blank=True, decimal_places=3, max_digits=5, null=True),
        ),
    ]
