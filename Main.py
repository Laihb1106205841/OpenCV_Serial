#from OpenCV_Serial import FOROUT
#import OpenCVt
import Communication.Web

print("连接到命令层！")


def sayHello():
    str = "hello"
    print(str)
    print(__name__ + 'from hello.sayhello()')


def OpenCVa():
    print("发送命令a！")
    import OpenCV_Serial
    T = OpenCV_Serial.FOROUT()
    return T


def OpenCVb():
    print("发送命令b！")
    import Normal
    str = Normal.Time()
    return str

def InternetServer():
    str = Communication.Web.server()

def InternetClient():
    str = Communication.Web.client()


if __name__ == "__main__":
    print('This is main of module "hello.py"')
    sayHello()
    print(__name__ + 'from hello.main')
    OpenCVa()
