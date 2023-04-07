#from OpenCV_Serial import FOROUT
#import OpenCVt

print("连接到命令层！")


def sayHello():
    str = "hello"
    print(str)
    print(__name__ + 'from hello.sayhello()')


def OpenCVa():

    import OpenCV_Serial
    OpenCV_Serial.FOROUT()


def OpenCVb():
    print("\033[0;33;40m按钮发送命令成功！请稍等\033[0m")


if __name__ == "__main__":
    print('This is main of module "hello.py"')
    sayHello()
    print(__name__ + 'from hello.main')
    OpenCVa()
