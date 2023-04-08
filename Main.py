#from OpenCV_Serial import FOROUT
#import OpenCVt

print("连接到命令层！")


def sayHello():
    str = "hello"
    print(str)
    print(__name__ + 'from hello.sayhello()')


def OpenCVa():
    print("发送命令a！")
    import OpenCV_Serial
    OpenCV_Serial.FOROUT()


def OpenCVb():
    print("发送命令b！")
    import Normal
    Normal.Time()



if __name__ == "__main__":
    print('This is main of module "hello.py"')
    sayHello()
    print(__name__ + 'from hello.main')
    OpenCVa()
