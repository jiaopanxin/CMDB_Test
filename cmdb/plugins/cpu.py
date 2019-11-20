import subprocess
from plugins import allinfo
class Cpu(allinfo.run):
    def cmd_handle(self):
        tmp_d = {
            "cpu_model":self.run_cmd("sysctl -n machdep.cpu.brand_string | tr ' ' '_'"),
            "cpu_type":self.run_cmd("uname -p | tr ' ' '_'"),
            "cpu_num": self.run_cmd("sysctl -n machdep.cpu.arch_perf.number | tr ' ' '_'"),
            "cpu_cores": self.run_cmd("sysctl -n machdep.cpu.core_count | tr ' ' '_'")
            }
        return tmp_d
