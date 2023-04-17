from Communication import Server, Client

global string

def server(ip):
    print("开启服务器模式，ip地址为：")
    #import Server
    #while True:
    str = Server.socket_service_data(ip=ip)
    print(ip)

    return str

def client(ip):
    print("开启客户模式，ip地址为：")
    #import Client
    str = Client.sock_client_data(ip=ip)
    print(ip)

    return str





if __name__ == '__main__':
    print()
