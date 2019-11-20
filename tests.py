from multiprocessing import process
import django
import os
import sys
# 获取到项目的根目录
PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))

# 把项目的根目录放到 sys.path 中
sys.path.insert(0, PROJECT_ROOT)

# 设置环境变量
os.environ["DJANGO_SETTINGS_MODULE"] = "auto_cmdb.settings"
django.setup()

if __name__ == "__main__":
    import json
    from cmdb.models import Invertory_group
    inventory_group = Invertory_group.objects.all()

    # print(inventory_group.values("group_name","server__host_name","invertory_group__id=3"))
    print(inventory_group.filter(inventory_group__id=3))

    data = {}
    
    for group in inventory_group:  # 循环组
        data[group.group_name] = {}
        for variable_group in group.variable_group.all():  # 循环组的变量
            key = variable_group.variable_name.key  # 变量的key
            value = variable_group.variable_name.value  # 变量的value
            vars_obj = data[group.group_name].setdefault("vars", {})  # 创建对应的字典
            vars_obj[key] = value

        for group_hosts in group.server.all():
            hosts_obj = data[group.group_name].setdefault("hosts", [])
        hosts_obj.append(group_hosts.manager_ip)

    # print(json.dumps(data, indent=4))
