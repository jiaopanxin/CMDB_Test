#!/usr/bin/env  python3      #
import pprint
import sys
import os
import requests
import json

#查到本文件的路径的前两个目录的路径 （目的：调整搜索模块的路径的根目录）
Base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# 将查到的路径插入到搜索模块的路径集最前，使该路径作为搜索路径的首选
sys.path.insert(0, Base_dir)   

def post_data(data):   
     # 使用 Post 方法请求到cmbd/asset/ 页面 ， 并将下面传送的 info 数据信息序列化
     requests.post(url='http://127.0.0.1:8000/cmdb/asset/',data=json.dumps(data)) 

from core.main import main
if __name__ == "__main__":
     info = main()
     post_data(info)
     print(info)


