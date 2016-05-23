# 重要提醒
>此版本不再更新。现在提供了更新的版本。HlanWeb。具有微信，网页展示，终端一体的

# HlanV2说明
---
### HlanV2的诞生
距离上个版本发布已有近一周的时间了.我也是刚接触python不,接触Python的目的就是python在运维上可以实现自动化
### 比起V1
比起上一个版本.这个改动比较大

- [X] 模块化设计,上一个版本作为本版本的一个模块
- [X] shell支持多线程(实测20台服务器没使用多线程30秒,多线程12s)

### 使用方法
```shell
python hlan.py check.up.all		#v2.0.3新加 自动检查所需要依赖的模块.当不存在时候自动给安装上
-----------下面这些可以忽略了,不删除证明他们曾经来过-------------
pip install paramiko
pip install pyyaml
pip install flask				#v2.0.2新加.作为web框架使用
```

```python
#v2.0.0
python hlan.py 主机组 -m 模块名 -a "传递给模块的参数"
#v2.0.1 
python hlan.py 主机组.模块名.参数
#v2.0.2
python wh.py 			#默认是端口1995
Browser:http://localhost:1995/主机组.模块名.参数
eg:http://localhost:1995/my.shell.disk
```
### V2版本更新计划
1. SFTP传输上传下载文件
2. 发布项目
[开发文档](https://www.zybuluo.com/iyuesh/note/348373) ,写的有点烂.我慢慢改吧

####2016/04/27 V2.0.3
>1. 好吧.存在了3个版本的路径问题给解决了.比起以前那种写法高大上了........
>2. 入口规则自定义更加简单化了.详情见部分代码说明1
>3. 新添加了安装模块.使用起来更加简单化了.
>4. 上个版本遗留的问题.在python3.X上面运行报错的问题

####2016/04/21 V2.0.2
>1. 重写了了架构.改成三层架构
>2. 重写了shell模块.为了迎合web设计.返回数据类型为字典
>3.	添加web形式.现在控制台和web都能使用,框架使用的flask


####2016/04/16 V2.0.1
>1. 增加了入口规则自定义
>2. 增加了服务器连接端口功能

### 未来规划

* 支持ansible/ansible-playbook/salt等其他自动化工具(linux下)
* 支持项目clone,数据库导入导出

###部分代码说明(开发文档随着完善将发布)
>1. 自定义接收参数规则 ext/hlan.py(v2.0.3版本已经优化了.不需要你自己写了.只需要改动程序的一个参数)
```python
@extHlanMain(sp='.')                            #以什么做分割.v2.0.3
def main(argvs):
	......
#恢复之前的只需要将4-7行注释掉即可
def extHlanMain(func):
    def _extHlanMain(argvs): 
        li=argvs[1].split('.') #以.分割 hlan.py my.shell.disk
        li.insert(0,'hlan.py') #转换成以前的格式
        li.insert(2,'-m')      # hlan.py my -m shell -a disk
        li.insert(4,'-a')      #这样方便模块接收时候统一
        func(li)
    return _extHlanMain
```
> 2.服务器账号文件规则(conf/server.yml)
```yaml
test:                   #group:定义一组有相同特征的服务器
  127.0.0.1:            #ip
    - root              #user 
    - 123456            #passwd
    - 223               #port V2.0.1版本增加
  202.106.0.20:         #ip 
    - root 
    - 123456
```
> 3.shell模块添加(conf/module.yml)
```yaml
ip:                 #将一组命令命名
- ip addr show      #command
mem:
- free -m
disk:
- df -Th
hostname:
- hostname
cd-tmp:
- cd /tmp && pwd   #command1
- pwd              #command2
```