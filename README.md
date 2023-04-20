# 基于 OpenCV + Web + Serial 的时钟控制系统
## 作者
赖海斌

## 产品简介 
本产品利用OpenCV图像识别库，建立了一个图像识别+串口通信的软件。

## 产品引用：
<p>pyserial包<p>
<p>python-OpenCV库<p>
<p>threading包<p>

## 版本
1.2.2

## 工程量
约700行

## 如何使用
#### ① 打开GUI ，出现4个按钮和一个文本输入框还有文本显示屏
#### <p>② 文本输入框内为您电脑的ip地址
#### <p>③ 点击“人脸计时”按钮开启OpenCV人脸识别，驱动时钟转动
#### <p>④ 点击“时钟模式”按钮开启时钟计时
#### <p>⑤ 点击“网络服务器”，变成网络服务器，准备接受客户信息
#### <p>⑥ 点击“网络客户端”，连接服务器，向服务器发送以下信息有以下功能：
<p>  发送“1”，开启服务器的人脸识别功能，控制服务器时钟
<p>  发送“2”，开启服务器的时钟计时功能，控制服务器时钟
<p>  发送“3”，开启客户端的人脸识别系统，控制服务器的时钟

## 许可证：MIT license
<cite>
The MIT License (MIT)
Copyright (c) <2023>  Author
Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the “Software”), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
The Software is provided “as is”, without warranty of any kind, express or implied, including but not limited to the warranties of merchantability, fitness for a particular purpose and noninfringement. In no event shall the authors 
or copyright holders be liable for any claim, damages or other liability, whether in an action of contract, tort or otherwise, arising from, out of or in connection with the software or the use or other dealings in the Software.
</cite>