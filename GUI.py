from tkinter import *
#import os
import Main


#import sys

#  获取py 文件所在目录(报错时尝试)
#current_path = os.path.dirname(__file__)

#  把这个目录设置成工作目录
#os.chdir(current_path)

class GUI():

    ip = '127.18.1.92'

    def __init__(self):
        root = Tk()  # 创建根窗口
        root.title('基于OpenCV的时钟控制系统')
        root.geometry("400x400")
        root.iconbitmap('favicon (8).ico')
        root.resizable(True, True)
        print("GUI打开成功！")
        G.conditions(self=self,root=root)

    def conditions(self,root):

        condition1 = Button(root, text='人脸计时', bg='yellow', activebackground='red', command=Open1)
        #fg_color = Button(root, text='前景色', fg='red')  # 设置按钮的前景色
        condition1.config(state=NORMAL)

        condition2 = Button(root, text='时钟模式', bg='yellow', activebackground='red', command=Open2)
        condition2.config(state=NORMAL)

        condition3 = Button(root, text='网络服务器模式', bg='yellow', activebackground='red', command=Open3a)
        condition3.config(state=NORMAL)

        condition4 = Button(root, text='网络客户端模式', bg='yellow', activebackground='red', command=Open3b)
        condition4.config(state=NORMAL)

        global entry
        entry_var = StringVar()
        entry_var.set('127.18.1.92')
        entry = Entry(root, width=40, textvariable=entry_var)
        global ip
        ip = entry.get()

        # 创建多行文本控件
        global t
        t = Text(root)

        t.place(x=0,y=150)
        entry.place(x=50, y=100)
        condition1.place(x=50,y=10)
        condition2.place(x=50,y=50)
        condition3.place(x=200,y=10)
        condition4.place(x=200,y=50)

        root.mainloop()  # 持续展示

    def GUi(self):
        print()


def Open1():
    print("激活按钮1！")
    t.insert("insert","开启人脸计时！\n")
    T = Main.OpenCVa()
    Str1 = '人脸出现了',T,'秒'

    t.insert("insert", Str1)
    t.insert("insert", "\n")


def Open2():
    print("激活按钮2！")
    str = Main.OpenCVb()
    t.insert("insert", str)
    t.insert("insert", "\n")

def Open3a():
    ip = entry.get()
    var = Main.InternetServer(ip)

    if(var == '3'):
        s = Main.Ser()
        m = "识别人脸：",s,"秒"
        t.insert("insert", "远程操作：")
        t.insert("insert", "\n")
        t.insert("insert", m)
        t.insert("insert", "\n")

    else:
        t.insert("insert", "远程操作：")
        t.insert("insert", "\n")
        t.insert("insert", var)
        t.insert("insert", "\n")


def Open3b():
    ip = entry.get()
    var = Main.InternetClient(ip)
    if (var == '3'):
       s = Main.Cli()

    t.insert("insert", var)
    t.insert("insert", "\n")


def getEntry():
    var = entry.get()
    print(var)


if __name__ == '__main__':

    G = GUI
    G.__init__(G)

    print("GUI关闭！")
