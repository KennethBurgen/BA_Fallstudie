# Generated by Django 4.2.11 on 2024-05-04 08:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UploadFileApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uploadedfile',
            name='file',
            field=models.FileField(upload_to=''),
        ),
    ]
