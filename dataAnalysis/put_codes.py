import paramiko,os,sys

server_dir = r"/root/zfrFile/python"  #需要下载远程服务器的目标文件夹路径
local_dir = r"./" #要保存文件的路径

hostname = '172.16.101.190'  #服务器IP地址
username = 'root'     # 登录账号
# password = 'zhaojjurbancomputing'     #登录密码
port = 8824

if __name__ == '__main__':

    private_key = paramiko.RSAKey.from_private_key_file(r'C:\Users\Administrator\.ssh\id_rsa',password="94qusibani")
    transport = paramiko.Transport((hostname, port))
    transport.connect(username=username, pkey=private_key)
    # transport = paramiko.Transport((hostname, port))
    # transport.connect(username=username, password=password)

    sftp = paramiko.SFTPClient.from_transport(transport)  # 如果连接需要密钥，则要加上一个参数，hostkey="密钥"

    file_list = os.listdir(local_dir)
    for i in file_list:
        # if "catBusO.py" in i:
        if "catBusO.py" in i:
            print("put: ",i)
            sftp.put(os.path.join(local_dir,i), server_dir + "/" + i)  # 将本地的Windows.txt文件上传至服务器/root/Windows.txt

    transport.close()  # 关闭连接
