# Generated by Django 3.2 on 2021-04-22 12:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('booklets', '0003_auto_20210422_1134'),
    ]

    operations = [
        migrations.CreateModel(
            name='Summary',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=1048)),
            ],
        ),
        migrations.AddField(
            model_name='booklet',
            name='summary',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='booklets.summary'),
        ),
    ]
