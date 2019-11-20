import subprocess
import os,sys

class run():
    def run_cmd(self,cmd):
        stat, result = subprocess.getstatusoutput(cmd)
        if not stat:
            return self.parse(result) 
    
    def parse(self,data):
        if data.endswith('_'):
            data =  data[:-1]
        return data





    
