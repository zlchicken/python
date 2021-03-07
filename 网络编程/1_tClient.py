"""
@version: python3.7
@Author  : ZL
@Explain :
@Time    : 2021/2/28 21:33
@File    : tClient_1
@Software: PyCharm
"""
from twisted.internet import protocol, reactor

HOST = '127.0.0.1'
PROT = 14030


class TSClntProtocol(protocol.Protocol):
    def sendData(self):
        data = input("> ")
        if data:
            print("sending....", data)
            self.transport.write(data.encode())
        else:
            self.transport.loseConnection()

    def connectionMade(self):
        self.sendData()

    def dataReceived(self, data):
        print(data)
        self.sendData()


class TSClntFactory(protocol.ClientFactory):
    protocol = TSClntProtocol
    clientLost = clientFailed = lambda self, connector, reason: reactor.stop()


reactor.connectTCP(HOST, PROT, TSClntFactory())
reactor.run()
