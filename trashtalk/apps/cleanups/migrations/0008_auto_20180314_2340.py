# Generated by Django 2.0.2 on 2018-03-14 23:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cleanups', '0007_auto_20180214_0432'),
    ]

    operations = [
        migrations.CreateModel(
            name='CleanupTools',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=1)),
                ('cleanup', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cleanups.Cleanup')),
            ],
        ),
        migrations.CreateModel(
            name='Tool',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('available', models.BooleanField(default=True)),
            ],
        ),
        migrations.AddField(
            model_name='cleanuptools',
            name='tool',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cleanups.Tool'),
        ),
    ]