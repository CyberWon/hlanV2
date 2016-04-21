#coding:utf-8
from threading import Thread
from mod.shell import execModule
from ext.conf import readServer,readProject
def mod_help(): #模块帮助,
    print 'python hlan.py test -m tomcat -a list #Show Project\npython hlan.py  test -m tomcat -a projectNum'
def out(gen): #遍历生成器函数
    for i in gen:
        if i:
            print i
def projectExec(ip,v,p):
    try:
        execModule(p['stop'], ip, v, sh=True)
    except Exception,e:
        print '%s:%s' %(ip,e)
    finally:
        pass
def projectStart(p): #选择项目后开始处理的函数 
    T_thread=[]
    rs=readServer(p['host'])
    for ip in rs:
        v=rs[ip]
        t=Thread(target=projectExec,args=(ip,v,p))
        T_thread.append(t)
    for i in range(len(T_thread)):
        t.setDaemon(True)
        T_thread[i].start()
def mod_main(argvs): #mod_main() hlan定义模块必须.代表脚本将参数传递给模块的开始
    yield False #hlan定义mod_main()必须参数 . 因为hlan需要接受的返回结果为生成器.
    try:
        if argvs[5]=='list':   #当list 请求时 列出模块列表
            for index,mn in enumerate(readProject(1, pl=True)):
                print index,mn
        else:  #没发生错误时候就开始处理项目了
            s=readProject(argvs[5])
            if s:
                projectStart(s)
            else:
                print 'Project not exsit!' 
    except Exception,e: #当输入格式不对引发错误显示出模块的正确使用方法
        print e
if __name__=='__main__': #编写模块时候调试用
    argvs=['hlan.py','test','-m','tomcat','-a','test']
    out(mod_main(argvs))