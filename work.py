# -*- coding:utf-8 -*-
import itchat, time
from itchat.content import *

@itchat.msg_register([TEXT, MAP, CARD, NOTE, SHARING])
def text_reply(msg):
    itchat.send('%s: %s' % (msg['Type'], msg['Text']), msg['FromUserName'])

def work():
    #itchat.auto_login(enableCmdQR=True)
    itchat.auto_login(enableCmdQR=2)

    itchat.send('Hello, filehelper', toUserName='filehelper')
    itchat.send_image(fileDir='0.jpg', toUserName='zjm-forever')
    itchat.run()


if __name__ == '__main__':
    work()
