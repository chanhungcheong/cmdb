# Generated by Django 2.2.5 on 2021-09-22 03:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('assets', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vlan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=16, null=True, verbose_name='Vlan')),
                ('vlan_id', models.CharField(blank=True, max_length=16, null=True, verbose_name='Vlan号')),
                ('subnet', models.CharField(blank=True, max_length=48, null=True, verbose_name='网段')),
                ('gateway', models.CharField(blank=True, max_length=32, null=True, verbose_name='网关')),
                ('describe', models.TextField(blank=True, max_length=64, null=True, verbose_name='描述')),
            ],
            options={
                'verbose_name_plural': 'Vlan信息',
            },
        ),
        migrations.CreateModel(
            name='IPManage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hostname', models.CharField(blank=True, default='', max_length=64, null=True, verbose_name='设备名称')),
                ('ip_add', models.GenericIPAddressField(verbose_name='IP地址')),
                ('mac_add', models.CharField(default='', max_length=48, verbose_name='MAC地址')),
                ('creator', models.CharField(blank=True, default='', max_length=32, null=True, verbose_name='创建人')),
                ('create_time', models.DateTimeField(auto_now_add=True, null=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, null=True, verbose_name='更新时间')),
                ('describe', models.TextField(blank=True, max_length=64, null=True, verbose_name='描述')),
                ('asset_belong_system', models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.CASCADE, to='assets.Application', verbose_name='所属系统')),
                ('vlan', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='ip_manage.Vlan', verbose_name='Vlan')),
            ],
            options={
                'verbose_name_plural': 'IP地址管理',
            },
        ),
    ]
