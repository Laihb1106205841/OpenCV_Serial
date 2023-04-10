from tkinter import *
#import os
import Main
#import sys

#  获取py 文件所在目录(报错时尝试)
#current_path = os.path.dirname(__file__)

#  把这个目录设置成工作目录
#os.chdir(current_path)

class GUI():


    show = ''
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
        condition1.pack()  # 展示

        condition2 = Button(root, text='时钟模式', bg='yellow', activebackground='red', command=Open2)
        condition2.config(state=NORMAL)
        condition2.pack()

         # 创建多行文本控件
        global t
        t = Text(root)

        t.pack()

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


if __name__ == '__main__':

    G = GUI
    G.__init__(G)

    print("GUI关闭！")
