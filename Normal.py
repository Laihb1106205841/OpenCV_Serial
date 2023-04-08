import serial
import Serial



def Time():
    print("\033[0;33;40m按钮发送命令成功！请稍等\033[0m")

    try:
        global ser
        ser = serial.Serial()
        Serial.port_open_recv(ser=ser)  # 打开串口
    except:
        print("serial库调用失败！请检查serial库是否正确安装！")

    else:
        Sending()

def Sending():

    Serial.send("2",ser)

    Serial.port_close(ser)
    print("成功调为时钟模式！")
