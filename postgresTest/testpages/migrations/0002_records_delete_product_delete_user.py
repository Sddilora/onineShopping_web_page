# Generated by Django 4.2 on 2023-04-17 00:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testpages', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Records',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('region', models.CharField(max_length=20)),
                ('country', models.CharField(max_length=20)),
                ('item_type', models.CharField(max_length=20)),
                ('sales_channel', models.CharField(max_length=10)),
            ],
        ),
        migrations.DeleteModel(
            name='Product',
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]
