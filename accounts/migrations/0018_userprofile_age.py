# Generated by Django 3.0.5 on 2020-05-20 18:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0017_auto_20200520_1142'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='age',
            field=models.CharField(blank=True, max_length=12, null=True),
        ),
    ]
