# Generated by Django 3.1.6 on 2023-10-25 20:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='reusableitem',
            name='in_stock',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='reusableitem',
            name='price',
            field=models.DecimalField(decimal_places=2, default='0.00', max_digits=5),
        ),
    ]