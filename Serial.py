#from time import sleep
import serial  # 导入串口通信库

print("连接到通信层！")
def port_open_recv(ser):  # 对串口的参数进行配置

    OpenSer = 0
    ser.port = 'com3'
    ser.baudrate = 9600
    ser.bytesize = 8
    ser.stopbits = 1
    ser.parity = "N"  # 奇偶校验位
    print("尝试打开串口3")

    try:
        try:
            ser.open()
            if(ser.isOpen()):
                OpenSer = 3

        except:
            if(not ser.isOpen()):
                print("串口3打开失败，尝试打开串口4！")
                ser.port = 'com4'
                ser.open()
                if(ser.isOpen()):
                    OpenSer = 4

    except:
            try:
                if(not ser.isOpen()):
                    print("串口3,4都打开失败了，尝试打开串口2！")
                    ser.port = 'com2'
                    ser.open()
                    if(ser.isOpen()):
                        OpenSer = 2
            except:
                print("串口2打开失败！")


    finally:
        if(not ser.isOpen()):
            print("串口2,3,4全部木大，请重新检查串口连接！")
            print("在此键入您的串口运行速度：")
            ser.baudrate = input()
            print("在此输入您的串口（com1，com2等）")
            str = input()
            ser.port = str
            print("尝试打开串口")
            ser.open()
            OpenSer = str

    if (ser.isOpen()):
        print("成功打开串口",OpenSer,"!")

        return '打开串口',OpenSer
    else:
        print("打开失败！")
        return "打开串口失败！"


#  isOpen()函数来查看串口的开闭状态


def port_close(ser):
    try:
        ser.close()
        if(ser.isOpen()):
            print("串口关闭失败！")
        else:
            print("串口关闭成功！")
            return "串口关闭！"
    except:
        print("串口关闭失败！")


def send(send_data, ser):
    if(ser.isOpen()):
        ser.write(send_data.encode('utf-8'))  # 编码
        print("向串口发送数据成功", send_data)
        return "向串口成功发送数据", send_data
    else:
        print("发送失败！")
        return "发送失败！"


def Connect():
    try:
        global ser
        ser = serial.Serial()
        port_open_recv(ser=ser)  # 打开串口
    except:
        print("Serial库调用失败！请检查Serial库是否正确安装！")