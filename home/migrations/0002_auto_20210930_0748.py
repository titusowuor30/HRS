# Generated by Django 3.1.7 on 2021-09-30 14:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cardetails',
            options={'verbose_name_plural': 'Client Car Details'},
        ),
        migrations.AddField(
            model_name='reservation',
            name='car_detail',
            field=models.ForeignKey(blank=True, help_text='leave blank if you have no car', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='reservations', to='home.cardetails'),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='Phone',
            field=models.CharField(default='070000000000', max_length=15),
        ),
    ]
