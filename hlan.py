#!/usr/bin/python
#coding:utf-8
import sys
def main_help():
    return '''python hlan.py host-group /host-ip/host-name -m mod_name  -a 'mod_args'
    eg:python hlan.py 127.0.0.1 -m shell -a 'free -m'
'''
def get_main_path():
    return '%s/mod' % (sys.path[0])
def main(argvs):
    try:
        load_mod=__import__(argvs[3])
    except Exception,e:
        print '%s'%(main_help())
        exit()
    mod_out=load_mod.mod_main(argvs)
    for i in mod_out:
        if i==False:
            continue
        else:
            print i
if __name__=='__main__':
    sys.path.append(get_main_path())
    main(sys.argv)