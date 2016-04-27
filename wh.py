#!/usr/bin/python
#coding:utf-8
from flask import Flask
import hlan,sys,time
from ext import mod_sys                 #将屏幕输出到buffer
from ext.conf import MOD_DIR
app = Flask(__name__)

@app.route('/')
def index():
    return 'Hlan Web'
@app.route('/<g>')
def web_main(g):
    # show the user profile for that user
    sys.path.append(MOD_DIR)
    s=mod_sys.__redirection__()
    sys.stdout=s
    li=['hlan.py',g]
    hlan.main(li)
    while s.buff=='':
        continue
    time.sleep(1)
    res='<pre>%s</pre>' % (s.buff)
    return res
@app.route('/favicon.ico')
def favicon():
    return '123'
if __name__=='__main__':
    app.run(host='0.0.0.0', port=1995,debug=True)