"""
@version: python3.7
@Author  : ZL
@Explain :
@Time    : 2021/2/28 19:33
@File    : tServer_1
@Software: PyCharm
"""
from twisted.internet import protocol, reactor
from time import ctime

PROT = 14030


class TSServProtocol(protocol.Protocol):
    def connectionMade(self):
        clnt = self.clnt = self.transport.getPeer().host
        print(clnt)

    def dataReceived(self, data):
        print(data)
        self.transport.write(('[%s] %s' % (ctime(), data)).encode())


factory = protocol.Factory()
factory.protocol = TSServProtocol
print("等待连接。。。")
reactor.listenTCP(PROT, factory)
reactor.run()
