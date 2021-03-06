# Generated by Django 3.0.3 on 2020-03-07 15:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='department',
            options={'ordering': ['name', '-updated_at']},
        ),
        migrations.AlterModelOptions(
            name='employee',
            options={'ordering': ['first_name', '-updated_at'], 'verbose_name_plural': 'Employees'},
        ),
        migrations.AlterModelOptions(
            name='position',
            options={'ordering': ['name', '-updated_at']},
        ),
        migrations.AddField(
            model_name='employee',
            name='bio',
            field=models.TextField(blank=True, help_text='Enter employee bio', null=True),
        ),
        migrations.AlterField(
            model_name='department',
            name='name',
            field=models.CharField(help_text='Enter department name', max_length=250, unique=True, verbose_name='Department name'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='email',
            field=models.EmailField(help_text='Enter email', max_length=254, unique=True),
        ),
        migrations.AlterField(
            model_name='employee',
            name='first_name',
            field=models.CharField(help_text='Enter first name', max_length=25),
        ),
        migrations.AlterField(
            model_name='employee',
            name='last_name',
            field=models.CharField(help_text='Enter last name', max_length=25),
        ),
        migrations.AlterField(
            model_name='employee',
            name='middle_name',
            field=models.CharField(help_text='Enter midels name', max_length=25),
        ),
    ]
