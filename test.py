#coding=utf8
import itchat
from itchat.content import *

#itchat.auto_login(enableCmdQR=True)
itchat.auto_login(enableCmdQR=True)

@itchat.msg_register([TEXT, MAP, CARD, NOTE, SHARING])
def text_reply(msg):
    itchat.send('%s: %s' % (msg['Type'], msg['Text']), msg['FromUserName'])

@itchat.msg_register([TEXT, MAP, CARD, NOTE, SHARING], isGroupChat = True)
def group_text_reply(msg):
    if msg['Type'] == TEXT: #如果是群文字消息
        print(msg['isAt'])
        print(msg['ActualNickName'])
        print(msg['Content'])
        if msg['isAt'] == True :
            itchat.send(u'@%s\u2005I received: %s' % (msg['ActualNickName'], msg['Content']), msg['FromUserName'])
        else :
            print()
    elif msg['Type'] == NOTE : #如果是新人进群消息
        if "邀请" in msg['Content'] :
            strs = msg['Content'].split('邀请')
            inviter = strs[0][1:-1]
            invited = strs[1].split('加入了群聊')[0][1:-1]
            print(inviter)
            print(invited)
            #TODO sql
            #发送欢迎消息
            itchat.send(u'@%s\u2005 欢迎加入本群，私聊我免费获取%s' % (invited, "***"), msg['FromUserName'])

    newmyself = itchat.search_friends()
    newchatroom = itchat.search_chatrooms(userName=msg['FromUserName'])
    itchat.send('msg from group %s, content: %s' % ('***', msg['Content']), newmyself['UserName'])

# itchat.send('Hello, filehelper', toUserName='filehelper')
# itchat.send_image(fileDir='0.jpg', toUserName='zjm-forever')
itchat.run()
