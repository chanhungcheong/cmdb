##  基于Django的cmdb运维资产管理系统 
参考：https://gitee.com/attacker/cmdb/tree/master

### 环境
![Python](https://img.shields.io/badge/python-3.7.3-blue.svg?style=plastic)
![Django](https://img.shields.io/badge/django-2.2.5-blue.svg?style=plastic)
![Simpleui](https://img.shields.io/badge/simpleui-2.9-brightgreen.svg?style=plastic)




### 手动部署
```
cd cmdb
echo env_django >> .gitignore # 排除env环境上传至git
python3 -m venv env_django
# 创建env环境
source  env_django/bin/activate # 载入py环境

pip  install -i http://mirrors.aliyun.com/pypi/simple  --trusted-host mirrors.aliyun.com  -r install/requirements.txt
#安装pip包(阿里源)


python manage.py makemigrations 
# 为改动models创建迁移记录
python manage.py migrate 
# 同步数据库
python manage.py  createsuperuser
# 建立后台管理员帐号


python manage.py runserver 0.0.0.0:8080
#启动服务
```


