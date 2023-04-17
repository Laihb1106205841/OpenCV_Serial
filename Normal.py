import serial
import Serial

# -*- coding:utf-8 -*-
from colorama import init

init(autoreset=True)


def Time():
    print('\033[0;33;40m按钮发送命令成功！请稍等\033[0m')

    try:
        global ser
        ser = serial.Serial()
        str1 = Serial.port_open_recv(ser=ser)  # 打开串口
    except:
        print("serial库调用失败！请检查serial库是否正确安装！")

    else:
        strSend = Sending()

    str = '切换为时钟模式！'

    return str1,strSend,str

def Sending():

    strSend = Serial.send("2", ser)

    strEND = Serial.port_close(ser)

    print('\033[0;33;40m成功调为时钟模式！\033[0m')


    str2 = strSend
    return str2
