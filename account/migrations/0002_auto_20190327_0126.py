# Generated by Django 2.1.7 on 2019-03-26 20:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='deleted',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='user',
            name='token_created',
            field=models.DateTimeField(auto_now=True),
        ),
    ]