#!/usr/bin/python
#coding:utf-8
import paramiko
def mingling(command,ssh):
    try:
        stdin,stdout,stderr=ssh.exec_command(command)
        return stdout.read()
    except Exception,e:
        return str(e)
def lianjie(user='',passwd='',host='',port='22'):
    ssh=paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        ssh.connect(username=user,password=passwd,hostname=host)
    except Exception,e:
        print '%s:%s'%(host,e)
    finally:
        return ssh
def logs(logs_enable=True):
    if logs_enable:
        paramiko.util.log_to_file('logs/syslogin.log')

