import socket
import sys
import time

import cv2
import threading  # 多线程

import serial

import Communication.Client
import GUI
import OpenCV_Serial
import Serial



def client():
    ip = GUI.GUI.ip
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


            if(ip == '0'):
                s.connect(('127.0.0.1', 6665))  # 服务器和客户端都在一个系统下时使用的ip和端口
            else:
                try:
                    s.connect((ip, 6665))  #服务器和客户端在不同的系统或不同的主机下时使用的ip和端口，首先要查看服务器所在的系统网卡的ip
                except:
                    s.connect(('127.18.1.92',6665))
                    ip = '127.18.1.92'
                    print(ip)

        except socket.error as msg:
            print(msg)
            print(sys.exit(1))

        global HasFace
        if(HasFace):
            data = '6'  #输入要传输的数据
            s.send(data.encode())  #将要传输的数据编码发送，如果是字符数据就必须要编码发送
            print("发送成功！")

        time.sleep(1)
        s.close()

def OpenCVCam():
    global Running

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
            Running = False
            break

        elif( len(faces) > 0 ):
            global HasFace
            HasFace = True

        else:
            HasFace = False

def CliCam():
    global Tim
    Tim = 0
    threads = []
    global HasFace
    HasFace = False

    try:

        global face_cascade
        face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    except:
        print("脸部数据库导入失败！请检查CV2有没有装对，或者数据库路径有无问题！")


    try:
        global cap
        cap = cv2.VideoCapture(0)
        print("成功打开摄像头！")
    except:
        print("电脑摄像头未成功开启！你可能关闭了摄像头！")


    t1 = threading.Thread(target=OpenCVCam)
    threads.append(t1)
    t2 = threading.Thread(target=client)
    threads.append(t2)

    for t in threads:
        t.start()

    for t in threads:
        t.join()


def SerClo():
    global Ti
    Ti = 0
    ip = GUI.GUI.ip

    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

        if(ip == '0'):
            ip = '127.0.0.1'
            s.bind(('127.0.0.1', 6665))  # 在同一台主机的ip下使用测试ip进行通信
            #print(ip)
        else:
            try:
                s.bind((ip, 6665))  #在不同主机或者同一主机的不同系统下使用实际ip
                #print(ip)
            except:
                ip = '127.18.1.92'
                #s.bind(('127.18.1.92',6666))
                s.bind((ip,6665))
        print(ip)

        s.listen(10)
    except socket.error as msg:
        print(msg)
        sys.exit(1)
    print("Server open successfully!")
    print("Wait for Connection..................")
    global ser
    ser = serial.Serial()
    Serial.port_open_recv(ser=ser)

    while True:
        time.sleep(0.1)
        if(0xFF == ord('q')):
            break

        sock, addr = s.accept()
        buf = sock.recv(1024)  #接收数据
        buf = buf.decode()  #解码
        print("The data from " + str(addr[0]) + " is " + str(buf))

        if(str(buf) == '6'):

            Serial.send(send_data="1", ser=ser)

            Ti += 1
            time.sleep(0.05)

    Serial.port_close(ser=ser)
