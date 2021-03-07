"""
@version: python3.7
@Author  : ZL
@Explain :
@Time    : 2021/2/28 19:33
@File    : tServer
@Software: PyCharm
"""
from socketserver import (TCPServer as TCP, StreamRequestHandler as SRH)
from time import ctime

HOST = ''
PORT = 14030  #
BUFSIZ = 1024  # 缓冲区大小
ADDR = (HOST, PORT)


class MyRequestHandler(SRH):
    def handle(self):
        print(self.client_address)
        self.wfile.write(('[%s] %s' % (ctime(), self.rfile.readline())).encode())


tcpServer = TCP(ADDR,MyRequestHandler)
tcpServer.serve_forever()


