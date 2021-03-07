"""
@version: python3.7
@Author  : ZL
@Explain : redis订阅者模式的订阅者
@Time    : 2021/2/19 10:47
@File    : pub
@Software: PyCharm
"""

import os
import time
from redis import StrictRedis, ConnectionPool


class Sub(object):
    """
    通过订阅发布者信息,调用批处理,实现svn更新代码
    """

    def __init__(self):
        pool = ConnectionPool(host='127.0.0.5', port=6379, password='1qaz2wsx!', db=5)
        self.redis_conn = StrictRedis(connection_pool=pool)

    def subscribeKey(self, channelDescribe):
        sub = self.redis_conn.pubsub()
        sub.psubscribe(channelDescribe)
        sub.listen()
        while True:
            msg = sub.parse_response()
            # 将接收到的信息转为STR类型
            command = list(map(lambda i: i.decode() if isinstance(i, bytes) else i, msg), )
            if 4 == len(command):
                if command[-1] == "update_robot":
                    cmd = r"C:\robot_svn\script\update_robot.bat"
                    os.system(cmd)
                if command[-1] == "reboot_robot":
                    cmd = r"C:\robot_svn\script\reboot_robot.bat"
                    os.system(cmd)


if __name__ == '__main__':
    while True:
        try:
            sb = Sub()
            channelDescribe = "command"
            sb.subscribeKey(channelDescribe)
        except Exception as e:
            print("连接失败,10秒后重新连接")
            time.sleep(10)
