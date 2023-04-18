#from OpenCV_Serial import FOROUT
#import OpenCVt
import Communication.Web
# -*- coding:utf-8 -*-
from colorama import init

import OpenCV_Serial

init(autoreset=True)


print('\033[0;33;40m连接到命令层！\033[0m')

global NetString

def sayHello():
    str = "hello"
    print(str)
    print(__name__ + 'from hello.sayhello()')


def OpenCVa():
    print('\033[0;33;40m开启OpenCV与串口通信！\033[0m')
    import OpenCV_Serial
    T = OpenCV_Serial.FOROUT()
    return T


def OpenCVb():
    print('\033[0;33;40m开启连接串口通信层！\033[0m')
    import Normal
    str = Normal.Time()
    return str

def InternetServer(ip):
    str = Communication.Web.server(ip=ip)
    if(str == '2'):
        print("远程执行时钟模式！")
        st = OpenCVb()

        return st

    if(str == '1'):
        print("远程执行人脸识别！")
        st = OpenCVa()
        return '人脸出现了',st,'秒'

    return str

def InternetClient(ip):
    str = Communication.Web.client(ip=ip)

    return str


if __name__ == "__main__":
    print('This is main of module "hello.py"')
    sayHello()
    print(__name__ + 'from hello.main')
    OpenCVa()
