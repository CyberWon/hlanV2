#!/usr/bin/python
#coding:utf-8
import paramiko
def sftpConn(hostIP,hostPort,hostUser,hostPasswd):
    t=paramiko.Transport((hostIP,hostPort))
    t.connect(username=hostUser,password=hostPasswd)
    sftp=paramiko.SFTPClient.from_transport(t)
    return sftp
def sftpPut(sftp,remotePath,localPath):
    try:
        sftp.put(localPath,remotePath)
        return True
    except:
        return False
def sftpGet(sftp,remotePath,localPath):
    try:
        sftp.get(remotePath,localPath)
        return True
    except:
        return False
    