# Generated by Django 4.0.5 on 2022-11-06 20:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_commande'),
    ]

    operations = [
        migrations.AddField(
            model_name='commande',
            name='total',
            field=models.CharField(default='500', max_length=300),
            preserve_default=False,
        ),
    ]
