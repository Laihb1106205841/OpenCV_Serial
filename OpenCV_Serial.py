
import cv2
import threading  # 多线程

import serial  # 导入串口通信库
from time import sleep


def port_open_recv():  # 对串口的参数进行配置
    ser.port = 'com3'
    ser.baudrate = 9600
    ser.bytesize = 8
    ser.stopbits = 1
    ser.parity = "N"  # 奇偶校验位
    print("尝试打开串口3")

    try:
        ser.open()
    except:
        print("串口3打开失败，尝试打开串口4！")
        ser.port = 'com4'
        ser.open()

    if (ser.isOpen()):
        print("串口打开成功！")
    else:
        print("打开失败！")
#  isOpen()函数来查看串口的开闭状态


def port_close():
    ser.close()
    if(ser.isOpen()):
        print("串口关闭失败！")
    else:
        print("串口关闭成功！")


def send(send_data):
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
            send("1")
            i += 1
            print(i)
            sleep(1)


if __name__ == "__main__":

    ser = serial.Serial()

    threads = []
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

    eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')
# 调用摄像头摄像头
    cap = cv2.VideoCapture(0)

    port_open_recv()#打开串口

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
# for t in threads:  另一种写法
#     t.start()
# for t in threads:
#     t.join()

def FOROUT():

    ser = serial.Serial()

    threads = []
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

    eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')
    # 调用摄像头摄像头
    cap = cv2.VideoCapture(0)

    port_open_recv()  # 打开串口

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
