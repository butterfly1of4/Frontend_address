# Generated by Django 3.1.2 on 2020-10-30 21:41

from django.db import migrations, models
import django.db.models.deletion
import phone_field.models


class Migration(migrations.Migration):

    dependencies = [
        ('address', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='contact_phone_number',
            field=phone_field.models.PhoneField(max_length=31),
        ),
        migrations.AlterField(
            model_name='contact',
            name='contact_user',
            field=models.ForeignKey(default='user', on_delete=django.db.models.deletion.CASCADE, to='address.user'),
        ),
    ]