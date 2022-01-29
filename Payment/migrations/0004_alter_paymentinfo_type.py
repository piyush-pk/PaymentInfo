# Generated by Django 4.0.1 on 2022-01-29 16:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Payment', '0003_paymentinfo_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paymentinfo',
            name='type',
            field=models.CharField(choices=[('DEBIT', 'DEBIT'), ('CREDIT', 'CREDIT')], default='DEBIT', max_length=10),
        ),
    ]
