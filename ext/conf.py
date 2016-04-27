#!/usr/bin/python
#coding:utf-8
'''
读写配置文件
'''
import yaml,os,ConfigParser
BASE_DIR = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
MOD_DIR = os.path.join(BASE_DIR,'mod')
def readServer(sg,sl=False):                #sg ServerGroup 服务器组 sl ServerList 组列表
    with open(os.path.join(BASE_DIR,'conf/server.yml'),'r') as f:
        server=yaml.load(f)
    if sl:                                  #当ServerList为真时返回组,而不是组信息
        li=[]
        for i in server:
            li.append(i)
        return li
    if sg in server:
        gp=server[sg]                       #gp group 服务器组信息
        for i in gp:                        #默认22端口在配置文件不存在,所以手动添加到返回结果
            if len(gp[i])<3:
                gp[i].append(22)
        return gp
    return False                            #Server Group 不存在时返回False

def readModule(sg,sl=False):                #sg Shell Group 命令组 sl Server List 命令组列表
    with open(os.path.join(BASE_DIR,'conf/shell.yml'),'r') as f:
        s=yaml.load(f)
    if sl:                                  #当Server List 为True时,返回命令组列表而不是命令组          
        li=[]
        for i in s:
            li.append(i)
        return li
    if sg in s:
        return s[sg]
    return False                            #Shell Group 不存在时返回False

def readProject(pn,pl=False):               #pn Project Name 项目名 pl Project List 项目列表
    with open(os.path.join(BASE_DIR, 'conf/project.yml'),'r') as f:
        p=yaml.load(f)
    if pl:                                  #当Project List 为True时,返回命令组列表而不是命令组          
        li=[]
        for i in p:
            li.append(i)
        return li
    if pn in p:
        return p[pn]
    return False                            #Project List 不存在时返回False
def readFirewall(fn,fl=False):              #Firewall Group Name 防火墙组名 fl Firewall Group  List 防火墙组列表
    with open(os.path.join(BASE_DIR, '/conf/firewall.yml'),'r') as f:        
        ff=yaml.load(f)
    if fl:                                  #当fl为true时.返回防火墙组列表
        li=[]
        for i in ff:
            li.append(i)
        return fl
    if fn in ff:
        return ff[fn]
    return False
def requireMod():
    cf=ConfigParser.ConfigParser()
    cf.read(os.path.join(BASE_DIR,'conf/hlan.ini'))
    opts=cf.options('require_mod')
    dict_mod={}
    for i in opts:
        pk=cf.get('require_mod',i)
        if pk=='true':
            dict_mod[i]={'package':i}
        else:
            dict_mod[pk]={'package':i}
           
    return dict_mod
if __name__=='__main__':
    print requireMod()
    