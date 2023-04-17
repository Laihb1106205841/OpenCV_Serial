import socket
import sys
import Main
import time

def socket_service_data(ip):


    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

        if(ip == '0'):
            ip = '127.0.0.1'
            s.bind(('127.0.0.1', 6665))  # 在同一台主机的ip下使用测试ip进行通信
            #print(ip)
        else:
            try:
                s.bind((ip, 6665))  #在不同主机或者同一主机的不同系统下使用实际ip
                #print(ip)
            except:
                ip = '127.18.1.92'
                #s.bind(('127.18.1.92',6666))
                s.bind((ip,6665))
        print(ip)

        s.listen(10)
    except socket.error as msg:
        print(msg)
        sys.exit(1)
    print("Server open successfully!")
    print("Wait for Connection..................")

    while True:
        time.sleep(0.1)
        if(0xFF == ord('q')):
            return 'exit'


        sock, addr = s.accept()
        buf = sock.recv(1024)  #接收数据
        buf = buf.decode()  #解码
        print("The data from " + str(addr[0]) + " is " + str(buf))
        print("Successfully")
        return str(buf)
        # Main.NetString = str(buf)
        # time.sleep(0.5)
        # sock.close()
if __name__ == '__main__':
    socket_service_data()
