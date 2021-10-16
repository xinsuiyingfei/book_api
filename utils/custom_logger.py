# -*- coding: utf-8 -*-
import os
import logging
import time

'''
@File    :   custom_logger.py
@Time    :   2021/05/06 11:36:27
@Author  :   zhaowen
@Version :   1.0
@Desc    :   日志模块
'''

logging.info("")

class CustomLogger(object):
    # 调用此类时创建logger实例，属于静态方法，必须要有返回值
    def __new__(cls, *args, **kwargs):
        # 创建日志解析对象
        my_logger = logging.getLogger('my_logger')
        # 设置解析器的收集等级
        my_logger.setLevel('DEBUG')
        # 控制台输出收集器
        l_s = logging.StreamHandler()
        # 输出收集等级
        l_s.setLevel('DEBUG')
        # 日志文件输出收集器
        cur_time = time.strftime("%Y%m%d%H%M", time.localtime())
        main_path=os.getcwd()+'/logs/'
        if  not os.path.exists(main_path):#如果路径不存在
            os.makedirs(main_path)
        l_f = logging.FileHandler(os.getcwd()+'/logs/plate_{}.log'.format(cur_time),encoding='utf-8')
        # 输出收集等级
        l_f.setLevel('DEBUG')
        # 将控制台和日志文件收集器添加到日志解析器
        my_logger.addHandler(l_s)
        my_logger.addHandler(l_f)
        # 日志输出格式
        fmt = '%(asctime)s - [%(filename)s --> line:%(lineno)d] - %(levelname)s : %(message)s'
        # 日志输出对象
        f_m = logging.Formatter(fmt)
        # 设置控制台和日志文件的格式
        l_s.setFormatter(f_m)
        l_f.setFormatter(f_m)
        # 返回日志解析器
        return my_logger

# 创建日志对象，后续直接引用对象，避免重复创建对象，添加日志Handler，重复写日志
logger_cls = CustomLogger()

