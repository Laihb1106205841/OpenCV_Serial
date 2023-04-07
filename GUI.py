from tkinter import *
#import os
import Main

#  获取py 文件所在目录(报错时尝试)
#current_path = os.path.dirname(__file__)

#  把这个目录设置成工作目录
#os.chdir(current_path)


def Open1():

    Main.OpenCVa()

def Open2():
    print("激活按钮2！")


def conditions(root):

    condition1 = Button(root, text='人脸计时', bg='yellow', activebackground='red', command=Open1)
    #fg_color = Button(root, text='前景色', fg='red')  # 设置按钮的前景色
    condition1.config(state=NORMAL)
    condition1.pack()  # 展示

    condition2 = Button(root, text='校准时钟', bg='yellow', activebackground='red', command=Open2)
    condition2.config(state=NORMAL)
    condition2.pack()



    root.mainloop()  # 持续展示


def GUi():
    root=Tk()#创建根窗口
    root.title('基于OpenCV的时钟控制系统')
    root.geometry("400x400")
    root.iconbitmap('favicon (8).ico')
    root.resizable(True,True)
    conditions(root=root)

if __name__ == '__main__':

    GUi()
    print("GUI关闭！")
