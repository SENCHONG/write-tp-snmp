
#!/usr/bin/env python
# -*- coding:utf-8 -*-

# 导入模块
import paramiko
import re
import json


def con_linux(hostname, username,  password):
    s = paramiko.SSHClient()
    # 取消安全认证
    s.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    # 连接linux
    s.connect(hostname=hostname, username=username, password=password)
    # 执行命令
    stdin, stdout, stderr = s.exec_command('lldpcli show neighbors | grep -E "Interface|SysName|---.*|PortID|PortDescr|MgmtIP.*\."')
    # 读取执行结果
    result = stdout.read()
    # 关闭linux连接
    s.close()
    # 返回执行结果
    return result


# 调用模块，传入liunx的ip/用户名/密码，并打印返回结果
res = con_linux(hostname='192.168.27.230', username='chensch',  password='pw@chensch').decode('utf-8')
res = re.split('---.*',res)
res = res[2:-1]
# print(res[0])
neighbors_res = []
for line in res:
    item_list = line.split('\n')[1:-1]
    tmp = {}
    for item_list_line in item_list:
        _item_list_line = item_list_line.split(': ')
        _item_list_line[0] = _item_list_line[0].strip()
        _item_list_line[1] = _item_list_line[1].strip()
        if _item_list_line[0] == 'Interface':
            _item_list_line[1] = (_item_list_line[1].strip().split(','))[0]
        tmp.update(
            {
                 _item_list_line[0]:  _item_list_line[1]
            }
        )
    neighbors_res.append(tmp)
    tmp = {}
neighbors_res = json.dumps(neighbors_res,indent=4,ensure_ascii=False)
print(neighbors_res)