# Register your models here.
from django.contrib import admin

# Register your models here.

from .models import Main, Domain


# 列表
class Domainlist(admin.ModelAdmin):
    # ordering = []
    list_display = ['host_record', 'domain', 'record_type', 'record_value', 'domain_describe']  # 分类
    list_filter = ['domain']  # 右侧过滤栏
    # list_editable = ['category'] #可编辑项

    empty_value_display = '无数据'  # 空数据
    # fk_fields = ('tags',) # 设置显示外键字段

    list_per_page = 100  # 每页显示条数

    search_fields = ['host_record', 'record_value']   # display 展示表字段，filter过滤分类，search搜索内容
    # date_hierarchy = 'publish' #按时间分类

    # exclude = ('view','comment','publish') # 排除字段
    fields = ('host_record', 'domain', 'record_type', 'record_value', 'domain_describe')  # 指定文章发布选项


# 分类展示
class Mainlist(admin.ModelAdmin):
    list_display = ['name', 'describe']  # 分类


admin.site.register(Domain, Domainlist)
admin.site.register(Main, Mainlist)
