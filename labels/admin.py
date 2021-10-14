from django.contrib import admin, messages
from labels.models import *
from import_export import resources
from import_export.admin import ImportExportActionModelAdmin
from django.utils.text import capfirst
from django.utils.html import format_html
from labels.scan_interface import *


class ProxyResource(resources.ModelResource):
    class Meta:
        model = Labels


@admin.register(Labels)
class Labelslist(ImportExportActionModelAdmin):
    resource_class = ProxyResource  # 支持导入导出
    # ordering = ['source']
    list_display = [
        'source',
        'destination',
        'describe',
        'manager',
        'create_time',
        'update_time',
        'edit_button',
    ]    # 分类
    list_filter = [
        'source',
        'destination',
        'describe',
        'manager',
        'create_time',
        'update_time',
    ]  # 右侧过滤栏
    # list_editable = ['describe'] #可编辑项
    # list_display_links = ['source', 'destination']
    empty_value_display = '-'  # 空数据
    # fk_fields = ('tags',) # 设置显示外键字段

    list_per_page = 200  # 每页显示条数

    search_fields = [
        'source',
        'destination',
        'describe',
        'manager',
        'create_time',
        'update_time',
    ]  # display 展示表字段，filter过滤分类，search搜索内容
    date_hierarchy = 'create_time'  # 按时间分类

    exclude = ('create_time', 'update_time')  # 排除字段
    # 在每行记录后面添加一个编辑的按钮

    def edit_button(self, edit_object):
        button_html = """<a class="changelink" href="/admin/labels/labels/%s/change/">编辑</a>""" % edit_object.id
        return format_html(button_html)

    edit_button.short_description = "编辑"


class MonitorDeviceslist(ImportExportActionModelAdmin):
    class ProxyResource(resources.ModelResource):
        class Meta:
            model = MonitorDevices
    resource_class = ProxyResource
    list_display = [
        'id',
        'device_name',
        'int_name',
        'int_ip',
        'int_status',
        'int_mac',
        'describe',
        'create_time',
        'update_time'
    ]
    list_filter = [
        'id',
        'device_name',
        'int_name',
        'int_ip',
        'int_status',
        'int_mac',
        'describe',
    ]  # 右侧过滤栏
    empty_value_display = '-'  # 空数据
    list_per_page = 200  # 每页显示条数
    search_fields = [
        'id',
        'device_name',
        'int_name',
        'int_ip',
        'int_status',
        'int_mac',
        'describe',
    ]  # display 展示表字段，filter过滤分类，search搜索内容
    date_hierarchy = 'create_time'  # 按时间分类

    exclude = ('create_time', 'update_time')  # 排除字段
    # def flush_ports(self, request, queryset):
    #     post = request.POST
    #     print("***************************************************************", post)
    #     if not request.POST.getlist('_selected_action'):
    #         print(
    #             "打印request.POST.get('_selected_action')：--------------------------------------------------------",
    #             request.POST.getlist('_selected_action')
    #         )
    #         ids = ScanDevices.objects.value_list('id')
    #         for device_id in ids:
    #             # 调用scan_ports函数进行接口扫描
    #             scan_ports(device_id)
    #         messages.add_message(request, messages.SUCCESS, '扫描完成，共扫描更新了{}台设备。'.format(len(ids)))
    #     elif request.POST.getlist('_selected_action'):
    #         ids = request.POST.getlist('_selected_action')
    #         for device_id in ids:
    #             scan_ports(device_id)
    #         messages.add_message(request, messages.SUCCESS, '扫描完成，共扫描更新了{}台设备。'.format(len(ids)))
    #     else:
    #         messages.add_message(request, messages.ERROR, '扫描失败！')
    #
    # flush_ports.short_description = '扫描设备接口'
    # flush_ports.type = 'primary'
    #
    # def test_action(self, request, queryset):
    #     pass
    # actions = ['flush_ports', 'test_action']
    # test_action.short_description = 'Test'


class ScanDeviceslist(ImportExportActionModelAdmin):
    class ProxyResource(resources.ModelResource):
        class Meta:
            model = ScanDevices
    resource_class = ProxyResource
    list_display = ['id', 'device_name', 'device_type', 'ip_address', 'port', 'describe']

    def flush_ports(self, request, queryset):
        if not request.POST.getlist('_selected_action'):
            ids = ScanDevices.objects.value_list('id')
            for device_id in ids:
                # 调用scan_ports函数进行接口扫描
                scan_ports(device_id)
            messages.add_message(request, messages.SUCCESS, '扫描完成，共扫描更新了{}台设备。'.format(len(ids)))
        elif request.POST.getlist('_selected_action'):
            ids = request.POST.getlist('_selected_action')
            for device_id in ids:
                scan_ports(device_id)
            messages.add_message(request, messages.SUCCESS, '扫描完成，共扫描更新了{}台设备。'.format(len(ids)))
        else:
            messages.add_message(request, messages.ERROR, '扫描失败！')

    flush_ports.short_description = '扫描设备接口'
    flush_ports.type = 'primary'
    actions = ['flush_ports']


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
# admin.site.unregister(Labels)
# admin.site.register(Labels, Labelslist)   # 厂家
admin.site.register(ScanDevices, ScanDeviceslist)   # 设备接口
admin.site.register(MonitorDevices, MonitorDeviceslist)   # 设备接口

admin.site.site_header = 'CMDB资产管理'
admin.site.site_title = 'CMDB资产管理'
