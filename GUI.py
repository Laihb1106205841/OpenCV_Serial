from tkinter import *
import os


def Open():
    os.system('OpenCV_Serial.py')




def conditions(root):
    condition = Button(root, text='活跃状态', bg='yellow', activebackground='red', command=Open)
    #fg_color = Button(root, text='前景色', fg='red')  # 设置按钮的前景色

    #condition.config(state=ACTIVE)
    condition.pack()  # 展示
    root.mainloop()  # 持续展示


def GUi():
    root=Tk()#创建根窗口
    root.geometry("400x400")
    root.resizable(False,False)
    conditions(root=root)

if __name__ == '__main__':
    GUi()
