# Generated by Django 5.0.6 on 2024-06-30 07:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_remove_student_file_remove_student_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('car_name', models.CharField(max_length=100)),
                ('speed', models.IntegerField()),
            ],
        ),
        migrations.DeleteModel(
            name='Proucts',
        ),
    ]
