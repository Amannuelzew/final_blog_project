# Generated by Django 5.0.3 on 2024-04-05 08:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_comment_email_comment_username_alter_comment_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='comment',
            field=models.TextField(max_length=300),
        ),
    ]