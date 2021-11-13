import sys
import pytest
from  utils.custom_logger import logger_cls
from utils.interface import http

'''
@File    :   conftest.py
@Time    :   2019/04/27 13:17:53
@Author  :   zhaowen
@Version :   1.0
@Desc    :   全局的前置条件和后置条件，每次执行时只会执行一次
'''



# def pytest_addoption(parser):    #pytest 运行时参数
#     parser.addoption(
#         "--setting",
#         action="store",
#         default='test33',
#         help="assign which env to use",
#     )


@pytest.fixture(scope='session', autouse=True)
def before_after(request):  # 前置条件和后置条件
    # http.set(request.config.option.setting)   #初始化环境信息   方法一，用pytest 的config
    http.set(sys.argv[1])   #方法二 利用python 自带的sys.argv 
    logger_cls.info("服务级-前置条件")
    http.login() #登录，不传用户名密码，则使用配置文件里的用户
    yield before_after  # 后置条件
    logger_cls.info("服务级-后置条件")




