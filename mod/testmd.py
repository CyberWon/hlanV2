#!/usr/bin/python
#coding:utf-8
from misaka import Markdown,HtmlRenderer
def main():
    with open('E:\User\Desktop/out.md','r') as f: 
        str=f.read()
    rndr = HtmlRenderer()
    md = Markdown(rndr)
    print(md(str))
if __name__=='__main__':
    main()