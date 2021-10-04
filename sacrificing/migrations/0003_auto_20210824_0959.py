# Generated by Django 3.2.6 on 2021-08-24 02:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sacrificing', '0002_buku_jumlah'),
    ]

    operations = [
        migrations.CreateModel(
            name='Kelompok',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=50)),
                ('keterangan', models.TextField()),
            ],
        ),
        migrations.AddField(
            model_name='buku',
            name='kelompok_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='sacrificing.kelompok'),
        ),
    ]
