# -*- coding: utf-8 -*-
import os

class Creat_folder():
    def creat_file(self,path1):
        isexit = os.path.exists(path1)
        if not isexit:
            os.makedirs(path1)
            print(path1 + ' 创建成功')
        else:
            print("已经存在！")