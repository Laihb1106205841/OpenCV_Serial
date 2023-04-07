
import cv2
import threading  # 多线程

import serial  # 导入串口通信库
from time import sleep


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
    else:
        print("打开失败！")
#  isOpen()函数来查看串口的开闭状态


def port_close(ser):
    ser.close()
    if(ser.isOpen()):
        print("串口关闭失败！")
    else:
        print("串口关闭成功！")


def send(send_data, ser):
    if(ser.isOpen()):
        ser.write(send_data.encode('utf-8'))  # 编码
        print("向串口发送数据成功", send_data)
    else:
        print("发送失败！")


def OpenCVCam():

    while (True):
        # 获取摄像头拍摄到的画面
        ret, frame = cap.read()
        faces = face_cascade.detectMultiScale(frame, 1.3, 5)
        img = frame
        for (x, y, w, h) in faces:
            # 画出人脸框，绿色，画笔宽度微
            img = cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

            # 还可以用人眼级联分类器引擎在人脸区域进行人眼识别，返回的eyes为眼睛坐标列表
            # 框选出人脸区域，在人脸区域而不是全图中进行人眼检测，节省计算资源
            #face_area = img[y:y + h, x:x + w]
            #eyes = eye_cascade.detectMultiScale(face_area)
        #  for (ex, ey, ew, eh) in eyes:
                # 画出人眼框，绿色，画笔宽度为1
            #    cv2.rectangle(face_area, (ex, ey), (ex + ew, ey + eh), (255, 0, 0), 1)

        # 实时展示效果画面
        cv2.imshow('frame2', img)
        # 每5毫秒监听一次键盘动作
        if cv2.waitKey(5) & 0xFF == ord('q'):
            break
        elif( len(faces) > 0 ):
            global HasFace
            HasFace = True

        else:
            HasFace = False


def Sending():
    i = 0
    while(True):

        global HasFace
        #print("执行sending！")
        #sleep(0.5)
        if (HasFace):
            send("1",ser)
            i += 1
            print(i)
            sleep(1)


# for t in threads:  另一种写法
#     t.start()
# for t in threads:
#     t.join()

def FOROUT():
    print("\033[0;33;40m按钮发送命令成功！请稍等\033[0m")



    threads = []

    try:
        global face_cascade
        face_cascade= cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    except:
        print("脸部数据库导入失败！请检查CV2有没有装对，或者数据库路径有无问题！")

    #  global eye_cascade  #眼睛模块，想用都可以用
    #  eye_cascade= cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')

    # 调用电脑摄像头
    try:
        global cap
        cap = cv2.VideoCapture(0)
        print("成功打开摄像头！")
    except:
        print("电脑摄像头未成功开启！你可能关闭了摄像头！")

    try:
        global ser
        ser = serial.Serial()
        port_open_recv(ser=ser)  # 打开串口
    except:
        print("Serial库调用失败！请检查Serial库是否正确安装！")






    global HasFace
    HasFace = False

    t1 = threading.Thread(target=OpenCVCam)
    threads.append(t1)
    t2 = threading.Thread(target=Sending)
    threads.append(t2)

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("退出！")

    # 最后，关闭所有窗口
    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    FOROUT()