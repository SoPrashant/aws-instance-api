# Generated by Django 4.2.5 on 2023-09-22 06:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login_credentials_api', '0002_remove_cloudlogin_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='cloudlogin',
            name='email_address',
            field=models.EmailField(default='prsharm7@cisco.com', max_length=254),
        ),
    ]