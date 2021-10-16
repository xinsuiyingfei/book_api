import requests
import yaml
from  utils.custom_logger import logger_cls
'''
@File    :   demo7.py
@Time    :   2021/09/13 20:40:19
@Author  :   wen
@Version :   1.0
@Desc    :   None
'''



class Interface:
    def __init__(self):
        self.host=""
        self.headers={"authorization":""}
        self.username=""
        self.password=""
        self.proxies = {'http': 'http://localhost:8888','https': 'http://localhost:8888'}  # 设置代理，调试时候定位问题使用

    def set(self,name="test1"):   #选择测试环境
        f = open("./utils/config.yaml", 'r')
        temp=yaml.load(f,Loader=yaml.FullLoader)  #Loader 不能执行方法
        self.host=temp[name]['host']
        self.headers={"authorization":""}
        self.username=temp[name]['username']
        self.password=temp[name]['password']    
        logger_cls.info(f"host:{self.host}")

    def login(self,username=None,password=None):
        try:
            if username:
                self.username=username
                self.password=password
            logger_cls.info(f"用户名:{username} 密码:{password}")
            res=requests.post(f"{self.host}api-token-auth/",{"username":self.username,"password":self.password})
            logger_cls.info(f"响应:{res.json()}")
            self.headers['authorization']="Token "+res.json()['token']
        except Exception as e:
            logger_cls.error(f"报错信息:{e}")

    def get(self,url,headers=None):
        res=""
        try:
            logger_cls.info(f"请求地址:{url}")
            if headers:
                self.headers.update(headers)   
            res=requests.get(f"{self.host}{url}",headers=self.headers)
            logger_cls.info(f"响应:{res.json()}")
            return res.json()
        except Exception as e:
            logger_cls.error(f"报错信息:{e} {res}")


    def post(self,url,body,headers=None):
        try:
            logger_cls.info(f"请求地址:{url} 请求参数:{body}")
            if headers:
                self.headers.update(headers)   
            res=requests.post(f"{self.host}{url}",json=body,headers=self.headers)
            # res=requests.post(f"{self.host}{url}",json=body,headers=self.headers,,proxies=self.proxies)
            # ,proxies=self.proxies 添加代理
            logger_cls.info(f"响应:{res.json()}")
            return res.json()
        except Exception as e:
            logger_cls.error(f"报错信息:{e} {res}")
       

    def put(self,url,body,headers=None):
        try:
            logger_cls.info(f"请求地址:{url} 请求参数:{body}")
            if headers:
                self.headers.update(headers)   
            res=requests.put(f"{self.host}{url}",json=body,headers=self.headers)
            logger_cls.info(f"响应:{res.json()}")
            return res.json()
        except Exception as e:
            logger_cls.error(f"报错信息:{e} {res}")

    def delete(self,url,body,headers=None):
        try:
            logger_cls.info(f"请求地址:{url} 请求参数:{body}")
            if headers:
                self.headers.update(headers)   
            res=requests.delete(f"{self.host}{url}")
            logger_cls.info(f"响应:{res.json()}")
            return res.json()
        except Exception as e:
            logger_cls.error(f"报错信息:{e} {res}")


http = Interface()


if __name__ == '__main__':
    # t = Interface()
    # t.login("admin","123456")
    # t.get("api/book/?book_name=&format=json")

    pass
# import urllib3
# urllib3.disable_warnings()

# requests.post("https://testerhome.com/account/sign_in",{"username":"zhaowen","password":"123456"},verify=False)   #如果是https请求加verify=False，移除SSL认证


# res=requests.post("http://106.14.37.200:8000/api-token-auth/",{"username":"admin","password":"123456"},verify=False)
# print(res.json())
# token=f"Token {res.json()['token']}"
# res2=requests.get("http://106.14.37.200:8000/api/book/?book_name=&format=json",headers={"authorization":token})
# print(res2.json())

# response = requests.post("http://106.14.37.200:8000/api-token-auth/",
#                          {"username": "admin", "password": "123456"})
# print(response.json())
# authorization = response.json()['token']
# res2=requests.get("http://106.14.37.200:8000/api/book/?book_name=&format=json", headers={"authorization":"Token "+authorization})
# print(res2.json())

# 

# token="Token "+response.json()['token']
# response2=requests.get("http://106.14.37.200:8000/api/book/?book_name=&format=json",headers={"authorization":token})
# print(response2.json())
