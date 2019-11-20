#第一行:内置模块
import importlib

#第二行:第三方模块

#第三行:自定义模块
from conf.settings import PLUGINS_DIC as plugins    # 从settings模块中导入PLUGINS_DIC对象并起别名为plugins(方便输入)

server_info = {}
def main():
    for key, val in plugins.items():                # 循环提前做好的存放数据的文件的路径的字典的键值
        mod_path, cls_name = val.rsplit('.',1)      # 将字典的值(plugins.cpu.Cpu)切割 
        mod_obj = importlib.import_module(mod_path) # 以字符串方式导入mod_path对应的模块(路径)
        cls = getattr(mod_obj, cls_name)    # 获取mod_path模块中cls_name对象(类)
        if cls_name == 'Mem':
            obj = cls(True)
        else:
            obj = cls()                         # 实例化获得的类
        info = obj.cmd_handle()             # 调用类中的函数，并用变量info接收
        #print(info)
        server_info[key] = info
    return server_info

#### 这个模块是:实现对plugins包中的cpu,mem模块的调用 #####
