import xadmin
from .models import (Tag, TreeNode, IDC, Cabinet, Asset, Server,
                     Memory, Disk, Connection, Invertory_group, Variable,Variable2Group2Server)


class TreeNodeAdmin(object):
  # 设置显示的字段
    list_display = ('node_name', 'node_upstream')
  # 设置搜索的字段
    search_fields = ('node_name', 'node_upstream')
  # 设置过滤的字段
    list_filter = ('node_name', 'node_upstream')


class TagAdmin(object):
  # 设置显示的字段
    list_display = ('name', 'latest_date', 'create_at')
  # 设置搜索的字段
    search_fields = ('name', 'latest_date', 'create_at')
  # 设置过滤的字段
    list_filter = ('name', 'latest_date', 'create_at')


class IDCAdmin(object):
  # 设置显示的字段
    list_display = ('name', 'addr', 'phone', 'latest_date', 'create_at')
  # 设置搜索的字段
    search_fields = ('name', 'addr', 'phone', 'latest_date', 'create_at')
  # 设置过滤的字段
    list_filter = ('name', 'addr', 'phone', 'latest_date', 'create_at')


class CabinetAdmin(object):
  # 设置显示的字段
    list_display = ('name', 'idc', 'latest_date', 'create_at')
  # 设置搜索的字段
    search_fields = ('name', 'idc', 'latest_date', 'create_at')
  # 设置过滤的字段
    list_filter = ('name', 'idc', 'latest_date', 'create_at')


class AssetAdmin(object):
  # 设置显示的字段
    list_display = ('device_type_id', 'device_status_id',
                    'cabinet', 'node', 'tag', 'latest_date', 'create_at')
  # 设置搜索的字段
    search_fields = ('device_type_id', 'device_status_id',
                     'cabinet', 'node', 'tag', 'latest_date', 'create_at')
  # 设置过滤的字段
    list_filter = ('device_type_id', 'device_status_id',
                   'cabinet', 'node', 'tag', 'latest_date', 'create_at')


class ServerAdmin(object):
    # 设置显示的字段
    list_display = ('asset', 'os_name', 'machine', 'os_version', 'host_name', 'kernel',
                    'cpu_model', 'cpu_type', 'cpu_num', 'cpu_cores', 'latest_date', 'create_at')
  # 设置搜索的字段
    search_fields = ('asset', 'os_name', 'machine', 'os_version', 'host_name', 'kernel',
                     'cpu_model', 'cpu_type', 'cpu_num', 'cpu_cores', 'latest_date', 'create_at')
  # 设置过滤的字段
    list_filter = ('asset', 'os_name', 'machine', 'os_version', 'host_name', 'kernel',
                   'cpu_model', 'cpu_type', 'cpu_num', 'cpu_cores', 'latest_date', 'create_at')


class MemoryAdmin(object):
  # 设置显示的字段
    list_display = ('capacity', 'slot', 'model', 'speed',
                    'manufacturer', 'sn', 'server', 'latest_date', 'create_at')
  # 设置搜索的字段
    search_fields = ('capacity', 'slot', 'model', 'speed',
                     'manufacturer', 'sn', 'server', 'latest_date', 'create_at')
  # 设置过滤的字段
    list_filter = ('capacity', 'slot', 'model', 'speed',
                   'manufacturer', 'sn', 'server', 'latest_date', 'create_at')


class DiskAdmin(object):
    # 设置显示的字段
    list_display = ('slot_number', 'pd_type', 'raw_size', 'server')
  # 设置搜索的字段
    search_fields = ('slot_number', 'pd_type', 'raw_size', 'server')
  # 设置过滤的字段
    list_filter = ('slot_number', 'pd_type', 'raw_size', 'server')


class ConnectionAdmin(object):
     # 设置显示的字段
    list_display = ('user', 'password', 'port', "auth")
  # 设置搜索的字段
    search_fields = ('user', 'password', 'port', "auth")
  # 设置过滤的字段
    list_filter = ('user', 'password', 'port', "auth")


class Invertory_groupAdmin(object):
    list_display = ("group_name", "server")
    search_fields = ("group_name", "server")
    list_filter = ("group_name", "server")


class variableAdmin(object):
    list_display = ("key", "value")
    search_fields = ("key", "value")
    list_filter = ("key", "value")

class variablehostgroupAdmin(object):
    list_display = ("variable_name", "variable_group","variable_hosts")
    search_fields = ("variable_name", "variable_group","variable_hosts")
    list_filter = ("variable_name", "variable_group","variable_hosts")

xadmin.site.register(Variable, variableAdmin)
xadmin.site.register(Variable2Group2Server, variablehostgroupAdmin)
xadmin.site.register(TreeNode, TreeNodeAdmin)
xadmin.site.register(Tag, TagAdmin)
xadmin.site.register(IDC, IDCAdmin)
xadmin.site.register(Cabinet, CabinetAdmin)
xadmin.site.register(Asset, AssetAdmin)
xadmin.site.register(Server, ServerAdmin)
xadmin.site.register(Memory, MemoryAdmin)
xadmin.site.register(Disk, DiskAdmin)
xadmin.site.register(Connection, ConnectionAdmin)
xadmin.site.register(Invertory_group, Invertory_groupAdmin)
