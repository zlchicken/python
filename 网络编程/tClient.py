"""
@version: python3.7
@Author  : ZL
@Explain :
@Time    : 2021/2/28 19:42
@File    : tClient
@Software: PyCharm
"""
from socket import *

HOST = '127.0.0.1'
PORT = 14030  #
BUFSIZ = 1024  # 缓冲区大小
ADDR = (HOST, PORT)  # 绑定地址


while True:
    ss = socket(AF_INET, SOCK_STREAM)
    ss.connect(ADDR)
    data = input("> ")
    data = data+"\n"
    ss.send(data.encode())
    datas = ss.recv(BUFSIZ)
    print(datas.decode())