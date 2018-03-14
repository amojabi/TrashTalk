# Generated by Django 2.0.2 on 2018-03-14 23:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cleanups', '0009_auto_20180314_2341'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cleanuptools',
            options={'verbose_name_plural': 'cleanup tools'},
        ),
        migrations.AddField(
            model_name='tool',
            name='description',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='tool',
            name='image',
            field=models.ImageField(default='', upload_to=''),
            preserve_default=False,
        ),
    ]
