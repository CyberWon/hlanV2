#!/usr/bin/python
#coding:utf-8
import paramiko,time,threading
from time import sleep
class run_cmd(threading.Thread):
    def __init__(self,hostname=None,password=None,username=None,port=None,echo_cmd=None):
        threading.Thread.__init__(self)
        self.hostname=hostname
        self.password=password
        self.username=username
        self.port=port
        self.echo_cmd=echo_cmd
        self.thread_stop=False
    def run(self):
#         paramiko.util.log_to_file('logs/paramiko.log')
        s=paramiko.SSHClient()
        s.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        s.connect(hostname = self.hostname,username=self.username, password=self.password)
        stdin,stdout,stderr=s.exec_command(self.echo_cmd)
        print stdout.read()
        s.close()
    def stop(self):
        self.thread_stop=True
def testssh(user='',password='',ip='',port=22,sg='hostname'):
    for hostname in ip:
        cmd_thread=run_cmd(hostname,password,user,port,sg)
        print hostname
        cmd_thread.start()
        cmd_thread.stop()
        if (cmd_thread.isAlive()):
            cmd_thread.join()
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
        sleep(1)
        print chan.recv(65535)  
def mingling(command,ssh):
    try:
        stdin,stdout,stderr=ssh.exec_command(command)
        return stdout.read()
    except Exception,e:
        return str(e)
def cmd(cmd,ssh):
    for m in cmd:
        stdin, stdout, stderr = ssh.exec_command(m)
        out = stdout.read()
        #屏幕输出
        print out
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
# if __name__=='__main__':
#     try:
#         ssh=testssh(user='root',password='neFtIoFoR2iKJqg81UvE',ip='192.168.60.5')
#     except Exception,e:
#         print e

