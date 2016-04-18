#!/usr/bin/python
#coding:utf-8
import paramiko,time
from time import sleep
def conn(user='',passwd='',ip='',port=22):
    t=paramiko.Transport((ip,port))
    t.connect(username=user,password=passwd)
    chan=t.open_session()
    chan.settimeout(40)
    chan.get_pty()
    chan.invoke_shell()
    cmds=['cd /var/log\n', 'ls\n']
    for cmd in cmds:
        chan.send(cmd)
        time.sleep(1)
        print chan.recv(65535)  
def mingling(command,ssh):
    try:
        stdin,stdout,stderr=ssh.exec_command(command)
        return stdout.read()
    except Exception,e:
        return str(e)
def lianjie(user='',passwd='',host='',port=22):
    ssh=paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        ssh.connect(username=user,password=passwd,hostname=host,port=port)
    except Exception,e:
        print '%s:%s'%(host,e)
    finally:
        return ssh
def logs(logs_enable=True):
    if logs_enable:
        paramiko.util.log_to_file('logs/syslogin.log')

