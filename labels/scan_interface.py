from netmiko import ConnectHandler
from labels.models import *


def scan_ports(device_id):
    scan_device = ScanDevices.objects.get(id=device_id)
    device_name = scan_device.device_name
    # 定义用于登录设备的信息字典
    device_login = {'device_type': scan_device.device_type,
                    'ip': scan_device.ip_address,
                    'username': scan_device.username,
                    'password': scan_device.password,
                    'port': scan_device.port}
    print(device_login)
    with ConnectHandler(**device_login) as connect:
        # 判断设备的类型，依据ntc_templates里面的类型进行分类
        if device_login['device_type'] == 'hp_comware':
            interfaces = connect.send_command('dis interface', use_textfsm=True)
            # print('interfaces:', interfaces)
            for interface in interfaces:
                # 检查接口是否已存在，存在则更新信息，不存在则创建完整记录
                MonitorDevices.objects.update_or_create(
                    device_name=device_name,
                    int_name=interface['interface'],
                    int_ip='',
                    int_status=interface['state'],
                    int_mac=interface['mac'],
                    describe=interface['des'],
                    defaults={
                        'device_name': device_name,
                        'int_name': interface['interface'],
                        'int_ip': '',
                        'int_status': interface['state'],
                        'int_mac': interface['mac'],
                        'describe': interface['des']
                    }
                )
        elif device_login['device_type'] == 'linux':
            interfaces = connect.send_command('ip address', use_textfsm=True)
            for interface in interfaces:
                # 进行mac地址转换，aa:bb:cc:dd:ee:ff转换成aabb-ccdd-eeff
                mac = str(interface['mac'])
                mac = list(mac.replace(':', ''))
                mac.insert(4, '-')
                mac.insert(9, '-')
                mac = ''.join(mac)
                # 检查接口是否已存在，存在则更新信息，不存在则创建完整记录
                MonitorDevices.objects.update_or_create(
                    device_name=device_name,
                    int_name=interface['int'],
                    int_ip=interface['ip'],
                    int_status=interface['state'],
                    int_mac=mac,
                    describe=interface['no'],
                    defaults={
                        'device_name': device_name,
                        'int_name': interface['int'],
                        'int_ip': interface['ip'],
                        'int_status': interface['state'],
                        'int_mac': mac,
                        'describe': interface['no']
                    }
                )
        elif device_login['device_type'] == 'cisco_ios_telnet':
            interfaces = connect.send_command('show interface', use_textfsm=True)
            for interface in interfaces:
                # 进行mac格式的转换，aaaa.bbbb.cccc转换成aaaa-bbbb-cccc
                mac = str(interface['address'])
                mac_covert = mac.replace('.', '-')
                # 检查接口是否已存在，存在则更新信息，不存在则创建完整记录
                MonitorDevices.objects.update_or_create(
                    device_name=device_name,
                    int_name=interface['interface'],
                    int_ip=interface['ip_address'],
                    int_status=interface['link_status'],
                    int_mac=mac_covert,
                    describe=interface['description'],
                    defaults={
                        'device_name': device_name,
                        'int_name': interface['interface'],
                        'int_ip': interface['ip_address'],
                        'int_status': interface['link_status'],
                        'int_mac': mac_covert,
                        'describe': interface['description']
                    }
                )
        else:
            print('设备类型不正确，无法登录到%s!' % (device_login[1]))
        connect.disconnect()
    return
