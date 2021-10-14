from django.db import models, transaction
# Create your models here.


class Labels(models.Model):
    """
    线缆信息管理
    """
    objects = models.Manager()

    source = models.TextField(max_length=64, blank=True, null=True, verbose_name='起点')
    destination = models.TextField(max_length=64, blank=True, null=True, verbose_name='终点')
    describe = models.TextField(max_length=64, blank=True, null=True, verbose_name='用途')
    manager = models.CharField(max_length=32, default='', null=True, blank=True, verbose_name="创建人")
    create_time = models.DateTimeField(auto_now_add=True, null=True, blank=True, verbose_name='创建时间')
    update_time = models.DateTimeField(auto_now=True, null=True, blank=True, verbose_name='更新时间')

    def __str__(self):
        return self.describe

    class Meta:
        verbose_name_plural = "线缆信息管理"


class ScanDevices(models.Model):
    objects = models.Manager()

    device_name = models.CharField(max_length=32, verbose_name='设备名称')
    device_type = models.CharField(max_length=32, verbose_name='设备类型')
    ip_address = models.CharField(max_length=32, verbose_name='管理IP')
    username = models.CharField(max_length=16, verbose_name='用户名')
    password = models.CharField(max_length=32, verbose_name='密码')
    port = models.CharField(max_length=16, default=22, null=True, blank=True, verbose_name='端口号')
    describe = models.TextField(max_length=128, blank=True, null=True, verbose_name='备注')

    def __str__(self):
        return self.device_name

    class Meta:
        verbose_name_plural = "设备清单"


class MonitorDevices(models.Model):
    objects = models.Manager()

    # port_status_choice = (
    #     (0, 'Dow'),
    #     (1, 'Up'),
    #  )  # 端口状态

    device_name = models.CharField(max_length=32, blank=True, null=True, verbose_name='设备名称')
    int_name = models.CharField(max_length=32, blank=True, null=True, verbose_name='接口名称')
    int_ip = models.CharField(max_length=48, blank=True, null=True, verbose_name='接口IP')
    int_status = models.CharField(max_length=32, blank=True, null=True, verbose_name='接口状态')
    int_mac = models.CharField(max_length=48, default='', blank=True, null=True, verbose_name='MAC地址')
    describe = models.TextField(max_length=128, blank=True, null=True, verbose_name='描述')
    create_time = models.DateTimeField(auto_now_add=True, null=True, blank=True, verbose_name='创建时间')
    update_time = models.DateTimeField(auto_now=True, null=True, blank=True, verbose_name='更新时间')

    def __str__(self):
        return self.device_name

    class Meta:
        verbose_name_plural = "设备接口"
