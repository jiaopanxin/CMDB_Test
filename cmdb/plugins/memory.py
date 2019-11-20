import subprocess
from plugins import allinfo
class Mem(allinfo.run):
    def __init__(self,debug):
        self.file = "/Users/mac/Library/Mobile\ Documents/com~apple~CloudDocs/python文件/R710-Memory-info"
        if debug:
            self.cmd = "grep -v '^$' %s" % self.file
        else:
            self.cmd = "dmidecode -q -t 17|grep -v '^$' "
        self.debug = debug

    def parse(self, data):
        info_mem = {}
        key_map = {
            'Size': 'capacity',
            'Locator': 'slot',
            'Type': 'model',
            'Speed': 'speed',
            'Manufacturer': 'manufacturer',
            'Serial Number': 'sn'
        }
        memory_list = [ mem for mem in data.split('Memory Device') if mem]

        for item in memory_list:
            single_slot = {}

            for line in item.splitlines():
                line = line.strip()
                if len(line.split(':')) == 2:
                    key, val = line.split(':')
                    key, val = key.strip(), val.strip()

                    if key in key_map:
                        single_slot[key_map[key]] = val

            info_mem[single_slot["slot"]] = single_slot
        return info_mem
    def cmd_handle(self):
        """获取R710数据接口"""
        return self.run_cmd(self.cmd)
