from django.db import models

# Create your models here.
from django.utils import timezone


# 记录类型  主机记录  记录值  备注

class Main(models.Model):  # 标签
    name = models.CharField(verbose_name='域名', max_length=100)
    describe = models.CharField(max_length=60, blank=True, null=True, verbose_name='备注')

    class Meta:
        verbose_name_plural = "域名"

    def __str__(self):
        return self.name


class Domain(models.Model):
    """    域名管理    """

    record_type_choice = (
        (0, 'A'),
        (1, 'CNAME'),
        (2, 'TXT'),
        (4, 'MX'),
        (5, 'MX'),
    )  # 类型

    host_record = models.CharField(max_length=64, verbose_name='主机记录')
    domain = models.ForeignKey('Main', verbose_name='域名', null=True, blank=True, on_delete=models.CASCADE)

    record_type = models.SmallIntegerField(choices=record_type_choice, default=0, verbose_name='记录类型')
    record_value = models.CharField(max_length=128, blank=True, null=True,  verbose_name='记录值')
    domain_describe = models.CharField(max_length=64, blank=True, null=True, verbose_name='备注')
    publish = models.DateTimeField(verbose_name='发布时间', default=timezone.now)     #发布时间
    mod_date = models.DateField(verbose_name='更新时间', auto_now=True)      #更新时间

    class Meta:
        verbose_name_plural = "解析记录"

    def __str__(self):
        return self.host_record