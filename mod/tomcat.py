#coding:utf-8
import os,yaml
from mod import mod_sftp
def mod_help(): #模块帮助,
    print 'python hlan.py test -m tomcat -a list #Show Project\npython hlan.py  test -m tomcat -a projectNum'
def out(gen): #遍历生成器函数
    for i in gen:
        if i:
            print i
def ServerList(server_ip):  #从服务器存储文件中读取
    with open('../conf/tomcat_server.yml') as f_server: #打开账号信息文件, 
        s_server=yaml.load(f_server)
    return list(s_server[server_ip])+s_server[server_ip].values() #将ip与其对应的账号密码用list返回
def projectStart(choice_project): #选择项目后开始处理的函数 
#     for (k,v) in choice_project.items():
#         print '%s:%s' %(k,v)
    print ServerList(choice_project['host'].split()[0])
def ReadProject(): #读取tomcat项目配置文件,并且返回
    with open('../conf/tomcat_project.yml') as f:
        s=yaml.load(f)
    return s
def ProjectList(s): #项目列表.使用生成器节省内存空间
    for k in s:
        yield k
def mod_main(argvs): #mod_main() hlan定义模块必须.代表脚本将参数传递给模块的开始
    yield False #hlan定义mod_main()必须参数 . 因为hlan需要接受的返回结果为生成器.
    try:
        s=ReadProject()
        if argvs[5]=='list':   #当list 请求时 列出模块列表
            out(ProjectList(s))
        elif argvs[5]=='help': #当help 请求时 触发异常
            raise Exception
        else:  #没发生错误时候就开始处理项目了
            projectStart(s[argvs[5]]) 
    except Exception,e: #当输入格式不对引发错误显示出模块的正确使用方法
        print e
if __name__=='__main__': #编写模块时候调试用
    argvs=['hlan.py','test','-m','tomcat','-a','rno-api']
    out(mod_main(argvs))