import cv2
import threading  # 多线程

import serial  # 导入串口通信库
from time import sleep

import Serial

Tim = 0

def port_open_recv(ser):  # 对串口的参数进行配置
    Serial.port_open_recv(ser=ser)


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


def Sending():
    global Tim
    i = 0
    global Running
    while(Running):

        global HasFace
        #print("执行sending！")
        #sleep(0.5)
        if (HasFace):
            Serial.send("1", ser)
            i += 1
            Tim +=1
            print(i)
            sleep(1)

# for t in threads:  另一种写法
#     t.start()
# for t in threads:
#     t.join()

def FOROUT():
    global Tim
    Tim = 0


    print("\033[0;33;40m按钮发送命令成功！请稍等\033[0m")
    print("按q可退出程序！")

    global Running
    Running = True

    threads = []

    try:

        global face_cascade
        face_cascade= cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
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

    Serial.port_close(ser)
    return Tim




if __name__ == "__main__":
    FOROUT()