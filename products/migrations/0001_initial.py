# Generated by Django 4.0.4 on 2022-04-14 15:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=2000)),
                ('price', models.DecimalField(decimal_places=2, max_digits=8)),
                ('inventory_quantity', models.IntegerField()),
            ],
        ),
    ]
