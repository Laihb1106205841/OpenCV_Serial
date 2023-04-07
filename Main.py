#from OpenCV_Serial import FOROUT
#import OpenCVt

print("GUI打开成功！")


def sayHello():
    str = "hello"
    print(str)
    print(__name__ + 'from hello.sayhello()')


def OpenCVa():

    print("\033[0;33;40m按钮发送命令成功！请稍等\033[0m")
    import OpenCV_Serial
    OpenCV_Serial.FOROUT()


def OpenCVb():
    print("\033[0;33;40m按钮发送命令成功！请稍等\033[0m")


if __name__ == "__main__":
    print('This is main of module "hello.py"')
    sayHello()
    print(__name__ + 'from hello.main')
    OpenCVa()
