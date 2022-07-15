import paramiko



hostname = '172.16.101.222'  #服务器IP地址
username = 'root'     # 登录账号
password = 'zhaojjurbancomputing'     #登录密码

start_port = 32770
end_port = 32780

if __name__ == '__main__':

    # for port in range(start_port,end_port):
    find_falg = False
    port = start_port
    while (port <= end_port and not find_falg):
        try:
            transport = paramiko.Transport((hostname, port))
            transport.connect(username=username, password=password)
            transport.close()  # 关闭连接
            print("find " + str(port))
            find_falg = True
        except:
            print(str(port) + " no")

        port += 1