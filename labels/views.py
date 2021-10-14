from netmiko import ConnectHandler
# from labels.models import *
import json
#
#
# # Create your views here.
#

sw1 = {
    'device_type': 'cisco_ios_telnet',
    'ip': '172.16.246.34',
    # 'device_type': 'hp_comware',
    # 'ip': '172.16.246.37',
    'username': 'gdsc',
    'password': 'gdsc@2014'
}
svr1 = {
    # 'device_type': 'cisco_ios_telnet',
    # 'device_type': 'hp_comware',
    'device_type': 'linux',
    'ip': '172.16.96.31',
    # 'ip': '172.16.246.37',
    # 'ip': '172.16.246.34',
    'username': 'root',
    # 'username': 'gdsc',
    'password': 'gd_scadmin@2725'
    # 'password': 'gdsc@2014'
}


# with ConnectHandler(**sw1) as connect:
#     # print("已经成功登陆交换机" + sw1['ip'])
#     display_int_brief = connect.send_command('show interface', use_textfsm=True)
#     # display_int_brief = connect.send_command('dis interface', use_textfsm=True)
#     # print(display_int_brief)
#     print(type(display_int_brief))
#     display_int_brief_json = json.dumps(display_int_brief, indent=2)
#     print(display_int_brief_json)
#
# with ConnectHandler(**svr1) as connect:
#     print("已经成功登陆服务器" + svr1['ip'])
#     display_int_brief = connect.send_command('ip address', use_textfsm=True)
#     display_int_brief_json = json.dumps(display_int_brief, indent=2)
#     print(display_int_brief_json)
#     connect.disconnect()
