#from OpenCV_Serial import FOROUT
#import OpenCVt

print("GUI打开成功！")


def sayHello():
    str = "hello"
    print(str);
    print(__name__ + 'from hello.sayhello()')

def OpenCVa():
    print("按钮command成功！")
    import OpenCV_Serial
    OpenCV_Serial.FOROUT()



if __name__ == "__main__":
    print('This is main of module "hello.py"')
    sayHello()
    print(__name__ + 'from hello.main')
    OpenCVa()
