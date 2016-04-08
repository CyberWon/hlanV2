#coding:utf-8
import os,json,mod_sftp

def ServerList(server_ip):
    f_server=file('conf/server.json')
    s_server=json.load(f_server)
    f_server.close()
    s_list=[]
    for (k,v) in s_server[server_ip].items():
        s_list.append(k)
        s_list.append(v)
    return s_list
def ProjectInfo(choice_project):
    for (k,v) in choice_project.items():
        print '%s:%s' %(k,v)
    server_list=ServerList(choice_project['host'])
    exec_start='%s%s' %(choice_project['path'],choice_project['start'])
    exec_stop='%s%s' %(choice_project['path'],choice_project['stop'])
    exec_remotedir='%s%s'%(choice_project['path'],choice_project['file'])
    #print '%s:%s'%(server_list[0],server_list[1])
    t=paramiko.Transport((choice_project['host'],22))
    t.connect(username=server_list[0],password=server_list[1])
    sftp=paramiko.SFTPClient.from_transport(t)
    sftp.put(choice_project['local_file'],exec_remotedir)
    t.close()
    ssh=paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(hostname=choice_project['host'],username=server_list[0],password=server_list[1])
    print u'上传成功'
    #执行的命令
    stdin,stdout,stderr=ssh.exec_command(exec_stop)
    print stdout.read()    
    stdin,stdout,stderr=ssh.exec_command(exec_start)
    print stdout.read()
    ssh.close()
def ReadProject():
    f=file('conf/project.json')
    s=json.load(f)
    f.close
    return s
def ProjectList(s):
    project_list=[]
    for k in s:
        project_list.append(k)
    return project_list
def PrintProject(project_list):
    project_index=0
    while project_index <len(project_list):
        print '%s.%s' %(project_index,project_list[project_index])
        project_index=project_index+1
def mod_main(*argvs):
    s=ReadProject()
    ProjectInfo(s[argvs[5]])
def main(*argvs):
    print u'项目列表'
    s=ReadProject()
    p_list=ProjectList(s)
    PrintProject(p_list)
    print u'输入项目编号'
    choice_index=input('Input:')
    ProjectInfo(s[argvs[5]])
if __name__=='__main__':
    main()
    