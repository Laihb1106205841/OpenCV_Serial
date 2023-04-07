#导入OpenCv人脸识别库
import cv2

import mainSerial
import serial#导入串口通信库
from time import sleep

ser = serial.Serial()

def port_open_recv():#对串口的参数进行配置
    ser.port='com4'
    ser.baudrate=9600
    ser.bytesize=8
    ser.stopbits=1
    ser.parity="N"#奇偶校验位
    ser.open()
    if(ser.isOpen()):
        print("串口打开成功！")
    else:
        print("串口打开失败！")
#isOpen()函数来查看串口的开闭状态



def port_close():
    ser.close()
    if(ser.isOpen()):
        print("串口关闭失败！")
    else:
        print("串口关闭成功！")

def send(send_data):
    if(ser.isOpen()):
        ser.write(send_data.encode('utf-8'))#编码
        print("发送成功",send_data)
    else:
        print("发送失败！")


#读取人脸模型库
face_cascade = cv2.CascadeClassifier('haarcascade_frontalcatface.xml')
#获取摄像头
cap = cv2.VideoCapture(0)

port_open_recv()#打开串口


while(True):

    #读取摄像头当前这一帧的画面  ret:True fase image:当前这一帧画面
    ret, img = cap.read()
    #图片进行灰度处理
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    # 人脸检测
    faces = face_cascade.detectMultiScale(gray,scaleFactor=1.5,minNeighbors=5)


    #绘制人脸框
    for(x,y,w,h) in faces:
        width = x+w
        height = y+h
        strok=2
        color=(255,0,0)
        cv2.rectangle(img,(x,y),(width,height),color,strok)


    cv2.imshow('face',img)
    if cv2.waitKey(20) & 0XFF == ord('q'):
        break

   # if (len(faces) > 0):
   #     send("1234567")
   #     sleep(1)

cap.release()
cv2.destroyAllWindows()

