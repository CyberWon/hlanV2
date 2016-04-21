# HlanV2˵��
---
### HlanV2�ĵ���
�����ϸ��汾�������н�һ�ܵ�ʱ����.��Ҳ�ǸսӴ�python��,�Ӵ�Python��Ŀ�ľ���python����ά�Ͽ���ʵ���Զ���
### ����V1
������һ���汾.����Ķ��Ƚϴ�

- [X] ģ�黯���,��һ���汾��Ϊ���汾��һ��ģ��
- [X] shell֧�ֶ��߳�(ʵ��20̨������ûʹ�ö��߳�30��,���߳�12s)

### ʹ�÷���
```shell
pip install paramiko
pip install pyyaml
pip install flask				#v2.0.2�¼�.��Ϊweb���ʹ��
```

```python
#v2.0.0
python hlan.py ������ -m ģ���� -a "���ݸ�ģ��Ĳ���"
#v2.0.1 
python hlan.py ������.ģ����.����
```
### V2�汾���¼ƻ�
1. SFTP�����ϴ������ļ�
2. ������Ŀ

####2016/04/21 V2.0.2
>1. ��д���˼ܹ�.�ĳ�����ܹ�
>2. ��д��shellģ��.Ϊ��ӭ��web���.������������Ϊ�ֵ�
>3.	���web��ʽ.���ڿ���̨��web����ʹ��,���ʹ�õ�flask
>4. [�����ĵ�](https://www.zybuluo.com/iyuesh/note/348373) ,д���е���.�������İ�


####2016/04/16 V2.0.1
>1. ��������ڹ����Զ���
>2. �����˷��������Ӷ˿ڹ���


### δ���滮

* ֧��ansible/ansible-playbook/salt�������Զ�������(linux��)
* ֧����Ŀclone,���ݿ⵼�뵼��

###���ִ���˵��(�����ĵ��������ƽ�����)
>1.�Զ�����ղ������� ext/hlan.py
```python
#�ָ�֮ǰ��ֻ��Ҫ��4-7��ע�͵�����
def extHlanMain(func):
    def _extHlanMain(argvs): 
        li=argvs[1].split('.') #��.�ָ� hlan.py my.shell.disk
        li.insert(0,'hlan.py') #ת������ǰ�ĸ�ʽ
        li.insert(2,'-m')      # hlan.py my -m shell -a disk
        li.insert(4,'-a')      #��������ģ�����ʱ��ͳһ
        func(li)
    return _extHlanMain
```
> 2.�������˺��ļ�����(conf/server.yml)
```yaml
test:                   #group:����һ������ͬ�����ķ�����
  127.0.0.1:            #ip
    - root              #user 
    - 123456            #passwd
    - 223               #port V2.0.1�汾����
  202.106.0.20:         #ip 
    - root 
    - 123456
```
> 3.shellģ�����(conf/module.yml)
```yaml
ip:                 #��һ����������
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