# Generated by Django 3.1.4 on 2021-01-02 16:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myForms', '0004_auto_20210102_2135'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mybooks',
            name='Book_Type',
            field=models.CharField(choices=[('3', 'Poetry'), ('2', 'Philosopy')], max_length=10),
        ),
    ]
