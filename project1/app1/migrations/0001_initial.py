# Generated by Django 2.2.4 on 2019-09-18 16:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SavingsAccount',
            fields=[
                ('acno', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('balance', models.DecimalField(decimal_places=2, max_digits=10)),
                ('password', models.CharField(max_length=30)),
            ],
        ),
    ]
