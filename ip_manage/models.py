from assets.models import Application
from django.db import models
# Create your models here.


class IPManage(models.Model):
    """    所有IP的共有数据表    """

    vlan = models.ForeignKey('Vlan', verbose_name='Vlan', null=True, blank=True, on_delete=models.CASCADE)
    hostname = models.CharField(max_length=64, default='', blank=True, null=True, verbose_name='设备名称')
    # ip_add = models.GenericIPAddressField(verbose_name='IP地址')   # 指定了ip类型
    ip_add = models.GenericIPAddressField(verbose_name='IP地址')   # 指定了ip类型
    mac_add = models.CharField(max_length=48, default='', verbose_name='MAC地址')
    asset_belong_system = models.ForeignKey(
        Application,  verbose_name='所属系统', default='', blank=True, null=True, on_delete=models.CASCADE)
    creator = models.CharField(max_length=32, default='', null=True, blank=True, verbose_name="创建人")
    create_time = models.DateTimeField(auto_now_add=True, null=True, blank=True, verbose_name='创建时间')
    update_time = models.DateTimeField(auto_now=True, null=True, blank=True, verbose_name='更新时间')
    describe = models.TextField(max_length=64, blank=True, null=True, verbose_name='描述')

    def __str__(self):
        return self.ip_add

    class Meta:
        verbose_name_plural = "IP地址管理"


class Vlan(models.Model):
    """
    VLAN
    """
    name = models.CharField(max_length=16, blank=True, null=True, verbose_name='Vlan')
    vlan_id = models.CharField(max_length=16, blank=True, null=True, verbose_name='Vlan号')
    subnet = models.CharField(max_length=48, blank=True, null=True, verbose_name='网段')
    gateway = models.CharField(max_length=32, blank=True, null=True, verbose_name='网关')
    describe = models.TextField(max_length=64, blank=True, null=True, verbose_name='描述')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Vlan信息"
