# Register your models here.
from django.utils.html import format_html

from django.contrib import admin
from assets.models import *
from import_export import resources
from import_export.admin import ImportExportActionModelAdmin
from django.utils.text import capfirst


class ProxyResource(resources.ModelResource):
    class Meta:
        model = Asset

class VirtualProxyResource(resources.ModelResource):
    class Meta:
        model = VirtualAsset



@admin.register(Asset)
class Assetlist(ImportExportActionModelAdmin):

    resource_class = ProxyResource  # 支持导入导出

    # ordering = []
    list_display = [
        'owner',
        'asset_num',
        'mac_add',
        'department',
        'area',
        'asset_type',
        'ip_add',
        'hostname',
        'mgt_ip_add',
        'asset_belong_system',
        'asset_criticality_choice',
        'asset_service_type',
        'asset_manager',
        'put_shelf_time',
        'edit_button',
    ]    # 分类
    list_filter = [
        'area',
        'company',
        'department',
        'owner',
        'asset_type',
        'asset_model',
        'mgt_ip_add',
        'asset_belong_system',
        'asset_criticality_choice',
        'asset_service_type',
        'asset_manager',
    ]  # 右侧过滤栏
    # list_editable = ['manufacturer'] #可编辑项
    empty_value_display = '-'  # 空数据
    # fk_fields = ('tags',) # 设置显示外键字段

    list_per_page = 200  # 每页显示条数

    search_fields = [
        'mac_add',
        'owner',
        'sn',
        'hostname',
        'ip_add',
        'company',
        'department',
        'asset_type',
        'asset_model',
        'mgt_ip_add',
    ]  # display 展示表字段，filter过滤分类，search搜索内容
    date_hierarchy = 'create_time'  # 按时间分类

    exclude = ('create_time', 'update_time')  # 排除字段
    # fields = (('title','category'),'body','tags')  # 指定文章发布选项
    # 在每行记录后面添加一个编辑的按钮

    def edit_button(self, edit_object):
        button_html = """<a class="changelink" href="/admin/assets/asset/%s/change/">编辑</a>""" % edit_object.id
        return format_html(button_html)

    edit_button.short_description = "编辑"

# 名称、备注
@admin.register(VirtualAsset)
class VirtualAssetlist(ImportExportActionModelAdmin):

    resource_class = VirtualProxyResource  # 支持导入导出

    # ordering = []
    list_display = [
        'area',
        'hostname',
        'ip_add',
        'os',
        'asset_criticality_choice',
        'asset_belong_system',
        'asset_service_type',
        'manager',
        'use_company',
        'use_owner',
         'put_shelf_time',
    ]    # 分类
    list_filter = [
        'area',
        'hostname',
        'ip_add',
        'os',
        'asset_criticality_choice',
        'asset_belong_system',
        'asset_service_type',
        'manager',
        'use_company',
        'use_owner',
    ]  # 右侧过滤栏
    # list_editable = ['manufacturer'] #可编辑项
    empty_value_display = '-'  # 空数据
    # fk_fields = ('tags',) # 设置显示外键字段

    list_per_page = 200  # 每页显示条数

    search_fields = [
        'area',
        'hostname',
        'ip_add',
        'os',
        'asset_criticality_choice',
        'asset_belong_system',
        'asset_service_type',
        'manager',
        'use_company',
        'use_owner',
     ]  # display 展示表字段，filter过滤分类，search搜索内容
    date_hierarchy = 'create_time'  # 按时间分类

    exclude = ('create_time', 'update_time')  # 排除字段
    # fields = (('title','category'),'body','tags')  # 指定文章发布选项


# 名称、备注

class Arealist(admin.ModelAdmin):
    list_display = ['id', 'name', 'subnet', 'describe']
# 分类排序


class Manufacturerlist(admin.ModelAdmin):
    list_display = ['id', 'name', 'manufacturer', 'contact', 'phone', 'describe']


class Applicationlist(ImportExportActionModelAdmin):
    class ProxyResource(resources.ModelResource):
        class Meta:
            model = Application
    list_display = ['id', 'name', 'app_manager', 'manager_phone', 'owner_cop', 'owner_manager', 'describe']


'''
class Labelslist(admin.ModelAdmin):
    list_display = ['source', 'destination', 'describe']
'''


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
# admin.site.register(Asset) # 资产
admin.site.unregister(Asset)
admin.site.register(Asset, Assetlist)  # 资产
admin.site.register(Area, Arealist)   # 区域
admin.site.register(Application, Applicationlist)   # 所属系统
admin.site.register(Manufacturer, Manufacturerlist)   # 厂家


admin.site.site_header = 'CMDB资产管理'
admin.site.site_title = 'CMDB资产管理'
