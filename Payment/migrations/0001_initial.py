# Generated by Django 4.0.1 on 2022-01-25 16:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PaymentInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=150)),
                ('aadhar', models.CharField(max_length=12)),
                ('mobile', models.CharField(max_length=10)),
                ('address', models.CharField(max_length=250)),
                ('time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
