"""
@version: python3.7
@Author  : ZL
@Explain : redis订阅者模式的发布者
@Time    : 2021/2/19 11:07
@File    : sub
@Software: PyCharm
"""
from redis import ConnectionPool, StrictRedis


class Pub(object):
    """
    发布信息
    """

    def __init__(self):
        pool = ConnectionPool(host='127.0.0.5', port=6379, password='1qaz2wsx!', db=5)
        self.redis_conn = StrictRedis(connection_pool=pool)

    def publishKey(self, channelDescribe):
        msg = "robot_update"
        self.redis_conn.publish(channelDescribe, msg)


if __name__ == '__main__':
    pb = Pub()
    channelDescribe = "command"
    pb.publishKey(channelDescribe)
