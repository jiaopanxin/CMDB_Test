from plugins import allinfo
import subprocess
class Base(allinfo.run):
    def parse(self,data):
        if data.endswith('_'):
            data =  data[:-1]
        return data
    def cmd_handle(self):
        result = {
            'os_name':self.run_cmd("uname -s |tr ' ' '_' ").strip(),
            'machine':self.run_cmd("uname -m | tr ' ' '_'").strip(),
            'os_version':self.run_cmd("sw_vers -productVersion | tr ' ' '_'"),
            'host_name':self.run_cmd("hostname | tr ' ' '_'"),
            'kernel':self.run_cmd("uname -rv | tr ' ' '_'").strip()
        }
        return result



