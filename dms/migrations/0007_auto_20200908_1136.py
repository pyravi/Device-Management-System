# Generated by Django 2.1.15 on 2020-09-08 06:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dms', '0006_dashboard'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dashboard',
            name='device_allocation',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dms.Device_allocation_manager', verbose_name='Device Allocation Manager'),
        ),
        migrations.AlterField(
            model_name='dashboard',
            name='device_list',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dms.Device_manager', verbose_name='Device Manager'),
        ),
        migrations.AlterField(
            model_name='dashboard',
            name='request_list',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dms.Request_manager', verbose_name='Request Manager'),
        ),
        migrations.AlterField(
            model_name='device_allocation_manager',
            name='assign_device',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='dms.Device_manager', verbose_name='Assign Device Name'),
        ),
        migrations.AlterField(
            model_name='images',
            name='device_image',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dms.Device_manager', verbose_name='Device Image'),
        ),
        migrations.AlterField(
            model_name='request_manager',
            name='assign_device',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='dms.Device_manager', verbose_name='Device Request or New Device'),
        ),
    ]
