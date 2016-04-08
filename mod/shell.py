#!/usr/bin/python
#coding:utf-8
from mod import mod_ssh
from threading import Thread
import yaml
def Author():
    return 'name:Hlan\nVersion:0.0.1'
def get_cpu():
    return '四核'

def ReadServer():
    with open('conf/server.yml','r') as f:
        s=yaml.load(f)
    return s
def GetServer(server_group,server):
    for i in server[server_group]:
        server_list=server[server_group][i]
        yield [i,server_list[0],server_list[1]]
def ReadModule():
    with open('conf/module.yml','r') as f:
        s=yaml.load(f)
    return s
def execModule(argvs,server,m):
    msg=''
    msgHeader=server[0]
    try:
        ssh=mod_ssh.lianjie(user=server[1],passwd=server[2],host=server[0])
        mLen=0
        while mLen <len(m[argvs[5]]):
            msg='%s\n%s'%(msg,mod_ssh.mingling(m[argvs[5]][mLen], ssh)[:-1])
            mLen=mLen+1
    except Exception,e:
        msg='%s:%s'%(msg,e)
    finally:
        ssh.close()
        print '%s:%s\n'%(msgHeader,msg)
def mod_main(argvs):
    server_conf=ReadServer()
    T_thread=[]
    m=ReadModule()
    for server in GetServer(argvs[1], server_conf):
        
#          execModule(argvs, server, m)
         
#         
        t=Thread(target=execModule,args=(argvs, server, m))
        T_thread.append(t)
    for i in range(len(T_thread)):
        t.setDaemon(True)
        T_thread[i].start()
        yield False
#         yield ''[:-2]
        
def mod_help():
    yield '''python hlan.py test -m shell -a 'get_cpu'
    
'''
if __name__=='__main__':
    li=['hlan.py', 'test','-m', 'shell', '-a', 'ip']
    for i in mod_main(li):
        print i