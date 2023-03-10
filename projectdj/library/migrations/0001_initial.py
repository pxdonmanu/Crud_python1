# Generated by Django 3.2.8 on 2023-01-11 03:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('pname', models.CharField(max_length=100)),
                ('image', models.ImageField(null=True, upload_to='images/', verbose_name='image')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
    ]
