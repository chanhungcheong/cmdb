from django.db import models

# Create your models here.


class Labels(models.Model):
    """
    线缆信息管理
    """
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
