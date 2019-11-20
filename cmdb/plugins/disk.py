import subprocess
from plugins import allinfo
class Disk(allinfo.run):
    def __init__(self):
        self.file = "/Users/mac/Library/Mobile\ Documents/com~apple~CloudDocs/python文件/R710-disk-info"
        self.cmd = "grep -v '^$' %s" % self.file
    def parse(self,data):
        """处理数据"""
        slot_num_li = []
        pd_type_li = []
        raw_size = []
        disk_info = {}
        for line in data.split('\n'):
            if line.strip().startswith('Slot Number'):
                slot_num_li.append(line.strip().split(':')[-1].strip().replace(' ','_'))
            if line.strip().startswith('PD Type'):
                pd_type_li.append(line.strip().split(':')[-1].strip().replace(' ','_'))
            if line.strip().startswith('Raw Size'):
                raw_size.append(line.strip().split(':')[-1].rsplit(' ',2)[-3].strip().replace(' ','_'))
        # print(slot_num_li,pd_type_li,raw_size)
        i = 0
        while i < len(slot_num_li):
            for x,y,z in zip(slot_num_li,pd_type_li,raw_size):
                disk_key = {'slot_number':'', 'pd_type':'', 'raw_size':''}
                disk_key['slot_number'] = x
                disk_key['pd_type'] = y
                disk_key['raw_size'] = z
                disk_info[x] = disk_key
                i += 1
        # print(disk_dic)
        return disk_info

    def cmd_handle(self):
        """获取R710数据接口"""
        return self.run_cmd(self.cmd)

    # def cmd_handle(self):
    #     with open('R710-disk-info','r',encoding='utf-8') as f_r:
    #         content = f_r.read()
    #         # print(content)
    #     return self.parse(content)

# obj = Disk()
# print(obj.cmd_handle())