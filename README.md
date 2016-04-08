# HlanV2说明
---
### HlanV2的诞生
距离上个版本发布已有近一周的时间了.我也是刚接触python不,接触Python的目的就是python在运维上可以实现自动化
### 比起V1
比起上一个版本.这个改动比较大

- [X] 模块化设计,上一个版本作为本版本的一个模块
- [X] shell支持多线程(实测20台服务器没使用多线程30秒,多线程12s)

### 使用方法

```python
python hlan.py 主机组 -m 模块名 -a "传递给模块的参数"
```
### V2版本更新计划
1. SFTP传输上传下载文件
### 未来规划

* 支持ansible/ansible-playbook/salt等其他自动化工具(linux下)
* 支持项目clone,数据库导入导出