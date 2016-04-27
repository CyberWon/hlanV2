#!/usr/bin/python
#coding:utf-8
from ext.mod_file import IPtablesFile
from ext.conf import readFirewall
def fIP(v,fx):
    fx='INPUT' if fx=='in' else 'OUPUT' 
    for i in xrange(len(v)):
        if '->' in v[i]:
            frl=v[i].split('->')
            frP=frl[1].split(':')
            frPort=frP[1].split()
            for Port in xrange(len(frPort)):
                print('$IPT -A %s -s %s -p %s --dport %s -j ACCEPT'%(fx,frl[0],frP[0],frPort[Port]))
            continue
        print("$IPT -A %s -s %s -j ACCEPT" % (fx,v[i]))
def fPORT(v,fx,pt):
    fx='INPUT' if fx=='in' else 'OUPUT' 
    for i in xrange(len(v)):
        print("$IPT -A %s -p %s --dport %s -j ACCEPT" % (fx,pt,v[i]))
def mod_main(argvs):
#     IPtablesFile(rules_one())
    fr=readFirewall('test')                 #fr firewall Rules 防火墙规则
    fin=fr['in']
    fIP(fin['ip'],'in')
    fPORT(fin['tcp'],'in','tcp')
if __name__=='__main__':
    mod_main('1')