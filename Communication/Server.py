import socket
import sys

def socket_service_data():
    print("请输入您的ip地址，按0开始本地调试模式：")
    ip = input()
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)


        if(ip == '0'):
            s.bind(('127.0.0.1', 6665))  # 在同一台主机的ip下使用测试ip进行通信
        else:
            try:
                s.bind((ip, 6665))  #在不同主机或者同一主机的不同系统下使用实际ip
            except:
                ip = '127.18.1.92'
                #s.bind(('127.18.1.92',6666))
                s.bind((ip,6665))

        s.listen(10)
    except socket.error as msg:
        print(msg)
        sys.exit(1)

    print("Wait for Connection..................")

    while True:
        sock, addr = s.accept()
        buf = sock.recv(1024)  #接收数据
        buf = buf.decode()  #解码
        print("The data from " + str(addr[0]) + " is " + str(buf))
        print("Successfully")
        # return buf
        # sock.close()
if __name__ == '__main__':
    socket_service_data()
