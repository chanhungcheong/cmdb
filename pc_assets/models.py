from django.db import models

# Create your models here.


class PCAssets(models.Model):
    """    所有资产的共有数据表    """
    asset_type_choice = (
        ('pc', '桌面电脑'),
        ('laptop', '笔记本电脑'),
        ('printer', '网络打印机'),
        ('scanner', '扫描仪'),
        ('pad', '平板电脑'),
        ('phone', '手机'),
        ('smart_device', '智能终端'),
        ('other', '其它')
    )  # 类型

    asset_status_choice = (
        (0, '在运'),
        (1, '停运'),
     )  # 状态

    asset_criticality_choice = (
        (0, '一般'),
        (1, '关注'),
        (2, '重要'),
        (3, '关键')
    )  # 重要程度
    # choices 用于页面上的选择框标签，需要先提供一个二维的二元元组

    area = models.ForeignKey('PCArea', verbose_name='区域', null=True, blank=True, on_delete=models.CASCADE)
    hostname = models.CharField(max_length=64, default='', blank=True, null=True, verbose_name='主机名')
    # ip_add = models.GenericIPAddressField(verbose_name='IP地址')   # 指定了ip类型
    ip_add = models.CharField(max_length=32, default='', blank=True, null=True, verbose_name='IP地址')
    mac_add = models.CharField(max_length=48, default='', verbose_name='MAC地址')

    manufacturer = models.ForeignKey(
        'PCManufacturer', default='其它', verbose_name='厂家', null=True, blank=True, on_delete=models.SET_DEFAULT)
    asset_use = models.CharField(max_length=64, default='', blank=True,  null=True, verbose_name='用途')
    asset_type = models.CharField(choices=asset_type_choice, max_length=64, default='pc', verbose_name="资产类型")

    company = models.CharField(max_length=128, default='', null=True, blank=True, verbose_name="公司")
    department = models.CharField(max_length=64, default='', null=True, blank=True, verbose_name="部门")
    owner = models.CharField(max_length=32, default='', null=True, blank=True, verbose_name="使用人")

    create_time = models.DateTimeField(auto_now_add=True, null=True, blank=True, verbose_name='创建时间')
    update_time = models.DateTimeField(auto_now=True, null=True, blank=True, verbose_name='更新时间')
    comment = models.TextField(max_length=256, default='', blank=True, verbose_name='备注')

    def __str__(self):
        if self.hostname:
            return self.hostname
        else:
            return self.mac_add

    class Meta:
        verbose_name_plural = "资产信息"
        ordering = ['-create_time']


class PCArea(models.Model):
    """所属区域"""
    name = models.CharField(max_length=64, default='', verbose_name="区域")  # xxx机房；阿里云xx区
    subnet = models.CharField(max_length=64, blank=True, null=True, default='', verbose_name="IP地址段")
    #   bandwidth = models.CharField(max_length=32, blank=True, null=True, default='', verbose_name='出口带宽')
    #   contact = models.CharField(max_length=16, blank=True, null=True, verbose_name='联系人')
    #   phone = models.CharField(max_length=32, blank=True, null=True, verbose_name='联系电话')
    #   address = models.CharField(max_length=128, blank=True, null=True, default='', verbose_name="机房地址")
    #   contract_date = models.CharField(max_length=30, verbose_name='合同时间')
    describe = models.TextField(max_length=128, blank=True, null=True, verbose_name='备注')

    #   needed_cabinet = models.BooleanField(default=True, verbose_name=u"是否需要渲染机架图")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "所属区域"


class PCManufacturer(models.Model):
    """
    供应商
    """
    name = models.CharField(max_length=32, blank=True, null=True, verbose_name='供应商')
    manufacturer = models.CharField(max_length=32, blank=True, null=True, verbose_name='制造商')
    contact = models.CharField(max_length=16, blank=True, null=True, verbose_name='联系人')
    phone = models.CharField(max_length=32, blank=True, null=True, verbose_name='联系电话')
    describe = models.TextField(max_length=128, blank=True, null=True, verbose_name='备注')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "供应商信息"
