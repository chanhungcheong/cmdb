# Register your models here.


from django.contrib import admin
from pc_assets.models import *
from import_export import resources
from import_export.admin import ImportExportActionModelAdmin
from django.utils.text import capfirst


class ProxyResource(resources.ModelResource):
    class Meta:
        model = PCAssets


@admin.register(PCAssets)
class PCAssetList(ImportExportActionModelAdmin):

    resource_class = ProxyResource  # 支持导入导出

    # ordering = []
    list_display = [
        'owner',
        'mac_add',
        'department',
        'area',
        'asset_type',
        'asset_use',
        'ip_add',
        'hostname',
        'create_time',
    ]    # 分类
    list_filter = [
        'area',
        'company',
        'department',
        'owner',
        'asset_type',
        'asset_use',
    ]  # 右侧过滤栏
    # list_editable = ['manufacturer'] #可编辑项
    empty_value_display = '-'  # 空数据
    # fk_fields = ('tags',) # 设置显示外键字段

    list_per_page = 200  # 每页显示条数

    search_fields = [
        'mac_add',
        'owner',
        'hostname',
        'ip_add',
        'company',
        'department',
        'asset_type',
        'asset_use',
    ]  # display 展示表字段，filter过滤分类，search搜索内容
    date_hierarchy = 'create_time'  # 按时间分类

    exclude = ('create_time', 'update_time')  # 排除字段
    # fields = (('title','category'),'body','tags')  # 指定文章发布选项


# 名称、备注
class PCAreaList(admin.ModelAdmin):
    list_display = ['id', 'name', 'subnet', 'describe']
# 分类排序


class PCManufacturerList(admin.ModelAdmin):
    list_display = ['id', 'name', 'manufacturer', 'contact', 'phone', 'describe']
# 分类排序


def find_model_index(name):
    count = 0
    for model, model_admin in admin.site._registry.items():
        if capfirst(model._meta.verbose_name_plural) == name:
            return count
        else:
            count += 1
    return count


def index_decorator(func):
    def inner(*args, **kwargs):
        templateresponse = func(*args, **kwargs)
        for app in templateresponse.context_data['app_list']:
            app['models'].sort(key=lambda x: find_model_index(x['name']))
        return templateresponse
    return inner


admin.site.index = index_decorator(admin.site.index)
admin.site.app_index = index_decorator(admin.site.app_index)


# 注册模块,前台显示
admin.site.unregister(PCAssets)
admin.site.register(PCAssets, PCAssetList)  # 资产
admin.site.register(PCArea, PCAreaList)   # 区域
admin.site.register(PCManufacturer, PCManufacturerList)   # 厂家


admin.site.site_header = 'CMDB资产管理'
admin.site.site_title = 'CMDB资产管理'
