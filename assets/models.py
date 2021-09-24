from django.db import models

# Create your models here.


class Asset(models.Model):
    """    所有资产的共有数据表    """
    objects = models.Manager()
    asset_type_choice = (
        ('cloud_host', '云主机'),
        ('virtual_machine', '虚拟机'),
        ('virtual_node', '虚拟宿主机'),
        ('container_node', '容器主机节点'),
        ('server', '物理机'),
        ('switch', '交换机'),
        ('route', '路由器'),
        ('firewall', '防火墙'),
        ('ips', '入侵防御设备'),
        ('lb', '负载均衡设备'),
        ('waf', '应用防火墙'),
        ('pc', '桌面电脑'),
        ('laptop', '笔记本电脑'),
        ('printer', '网络打印机'),
        ('app', '应用系统'),
        ('database', '数据库'),
        ('middleware', '中间件'),
        ('datastore', '存储设备'),
        ('san_switch', '光纤交换机'),
        ('byod', '智能终端'),
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

    area = models.ForeignKey('Area', verbose_name='区域', null=True, blank=True, on_delete=models.CASCADE)
    hostname = models.CharField(max_length=64, default='', blank=True, null=True, verbose_name='主机名')
    asset_num = models.CharField(max_length=64, default='', blank=True, null=True, verbose_name="资产编号")
    # ip_add = models.GenericIPAddressField(verbose_name='IP地址')  # 指定了ip类型
    ip_add = models.CharField(max_length=32, default='', blank=True, null=True, verbose_name='IP地址')
    mgt_ip_add = models.CharField(max_length=32, default='', blank=True, null=True, verbose_name='MGT地址')
    mac_add = models.CharField(max_length=48, default='', verbose_name='MAC地址')
    sn = models.CharField(max_length=128, default='', verbose_name="序列号")
    manufacturer = models.ForeignKey(
        'Manufacturer', default='', verbose_name='制造商', null=True, blank=True, on_delete=models.CASCADE)
    asset_model = models.CharField(max_length=64, default='', blank=True,  null=True, verbose_name='型号')
    asset_type = models.CharField(choices=asset_type_choice, max_length=64, default='pc', verbose_name="资产类型")

    asset_criticality_choice = models.SmallIntegerField(
        choices=asset_criticality_choice, default=0, verbose_name='重要程度')
    asset_belong_system = models.ForeignKey(
        'Application', verbose_name='所属系统', default='', blank=True, null=True, on_delete=models.CASCADE)
    asset_service_type = models.CharField(max_length=64, default='', blank=True, null=True, verbose_name='业务类型')
    asset_manager = models.CharField(max_length=32, default='', null=True, blank=True, verbose_name="系统管理员")
    status = models.SmallIntegerField(choices=asset_status_choice, default=0, verbose_name='设备状态')
    company = models.CharField(max_length=128, default='', null=True, blank=True, verbose_name="公司")
    department = models.CharField(max_length=64, default='', null=True, blank=True, verbose_name="部门")
    owner = models.CharField(max_length=32, default='', null=True, blank=True, verbose_name="使用人")

    cpu = models.CharField(max_length=64, default='', blank=True, null=True, verbose_name='CPU')
    memory = models.CharField(max_length=64, default='', blank=True, null=True, verbose_name='内存')
    disk = models.CharField(max_length=64, default='', blank=True, null=True, verbose_name='硬盘')

    cabinet = models.CharField(max_length=16, default='', null=True, blank=True, verbose_name='机柜号')
    u_height = models.CharField(max_length=16, default='', null=True, blank=True, verbose_name="u高")
    rail_num = models.CharField(max_length=16, default='', null=True, blank=True, verbose_name="导轨位置")

    put_shelf_time = models.DateField(verbose_name='上线时间')
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


class Area(models.Model):
    """机房"""
    name = models.CharField(max_length=64, default='', verbose_name="区域")   # xxx机房；阿里云xx区
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


class Application(models.Model):
    """应用系统"""
    name = models.CharField(max_length=64, unique=True, verbose_name="应用系统")   # 所属应用系统
    app_manager = models.CharField(max_length=32, default='', null=True, blank=True, verbose_name="系统管理员")
    manager_phone = models.CharField(max_length=16, blank=True, null=True, verbose_name='系统管理员电话')
    owner_cop = models.CharField(max_length=64, blank=True, null=True, default='', verbose_name='建设单位')
    owner_manager = models.CharField(max_length=32, default='', null=True, blank=True, verbose_name="业务管理员")
    owner_phone = models.CharField(max_length=16, blank=True, null=True, verbose_name='业务管理员电话')
#   address = models.CharField(max_length=128, blank=True, null=True, default='', verbose_name="机房地址")
#   contract_date = models.CharField(max_length=30, verbose_name='合同时间')
    describe = models.TextField(max_length=128, blank=True, null=True, verbose_name='系统用途')
    comment = models.TextField(max_length=256, default='', blank=True, verbose_name='备注')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "所属系统"


class Manufacturer(models.Model):
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


'''
class MonitorDevices(models.Model):
    object = models.Manager()

    port_status_choice = (
        (0, 'Down'),
        (1, 'Up'),
     )  # 端口状态

    device_name = models.CharField(max_length=32, blank=True, null=True, verbose_name='设备名称')
    port_type = models.CharField(max_length=32, blank=True, null=True, verbose_name='接口类型')
    port_id = models.CharField(max_length=8, blank=True, null=True, verbose_name='接口编号')
    port_status = models.CharField(choices=port_status_choice, default=0, verbose_name='接口状态')
    port_mac = models.CharField(max_length=48, default='', verbose_name='MAC地址')
    describe = models.TextField(max_length=128, blank=True, null=True, verbose_name='备注')
'''

'''
class Labels(models.Model):
    """
    设备接口
    """
    source = models.TextField(max_length=64, blank=True, null=True, verbose_name='起点')
    destination = models.TextField(max_length=64, blank=True, null=True, verbose_name='终点')
    describe = models.TextField(max_length=64, blank=True, null=True, verbose_name='用途')

    def __str__(self):
        return self.describe

    class Meta:
        verbose_name_plural = "设备接口"
'''



