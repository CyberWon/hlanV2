#!/usr/bin/python
#coding:utf-8
from flask import Flask
from flask import request
import hlan,sys,time
from ext import mod_sys
app = Flask(__name__)

@app.route('/')
def index():
    return 'Hlan Web'
@app.route('/<g>',methods=['GET', 'POST'])
def web_main(g):
    # show the user profile for that user
    sys.path.append(hlan.get_main_path())
    s=mod_sys.__redirection__()
    sys.stdout=s
    li=['',g]
    hlan.main(li)
    while s.buff=='':
        continue
    time.sleep(1)
    rs={''}
    return '<pre>%s</pre>' % (s.buff)
if __name__=='__main__':
    app.run(host='0.0.0.0', port=1995,debug=True)