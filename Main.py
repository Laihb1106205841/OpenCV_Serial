import OpenCV_Serial
import OpenCVt

print("first")


def sayHello():
    str = "hello"
    print(str);
    print(__name__ + 'from hello.sayhello()')


if __name__ == "__main__":
    print('This is main of module "hello.py"')
    sayHello()
    print(__name__ + 'from hello.main')
    OpenCV_Serial.FOROUT()

