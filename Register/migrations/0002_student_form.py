# Generated by Django 2.1.7 on 2019-05-14 10:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Register', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='form',
            field=models.CharField(choices=[('Form1', 'form1'), ('Form2', 'form2'), ('Form3', 'form3'), ('Form4', 'form4'), ('Unknown', 'unknown')], default='Unknown', max_length=10),
        ),
    ]