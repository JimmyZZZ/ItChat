# -*- coding:utf-8 -*-
import daemon,os,sys
from work import work
with daemon.DaemonContext():
    sys.stdin = open('/root/itchat/log.log','r')
    sys.stdout = open('/root/itchat/log.log','a+')
    sys.stderr = open('/root/itchat/log.log','a+')
    work()
