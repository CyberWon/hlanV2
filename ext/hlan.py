#coding:utf-8
'''
对hlan main的扩展
'''
def extHlanMain(func):
    def _extHlanMain(argvs):
        li=argvs[1].split('.')
        li.insert(0,'hlan.py')
        li.insert(2,'-m')
        li.insert(4,'-a')
        func(li)
    return _extHlanMain