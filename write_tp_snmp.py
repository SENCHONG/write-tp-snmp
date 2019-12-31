# -*-conding:utf-8-*-

import configparser
import json
from tp_core import snmp
from tp_core import ssh

def getData():
    res = {}
    config = configparser.ConfigParser()
    config.read('config.ini')
    config.sections()
    if "DEVICES" not in config or "DEFAULT" not in config:
        print("错误：缺乏配置文件")
        exit(1)
    ip_address_list = json.loads(config["DEVICES"]["address"])
    comu_str = config["DEFAULT"]["SnmpCommunityString"]
    for ip_address in ip_address_list:
        try:
            ip_address = ip_address.replace("\n", '')
            _flag = snmp.sysDescr(ip_address, comu_str)
            if 'Linux' in _flag or 'linux' in _flag:  # 是linux系统
                if config["COMMON_AUTH"]["auth"] == 'true':
                    uuid = json.loads(config["COMMON_AUTH"]["uuid"])[0].split('/')
                    _res = ssh.getSSH(ip_address, uuid[0], uuid[1])
                else:
                    uuid = json.loads(config["LINUX"]["uuid"])
                    for item in uuid:
                        _item = item.split('/')
                        if _item[0] == ip_address:
                            _res = ssh.getSSH(ip_address, _item[1], _item[2])
                            break
            else:  # 不是linux系统，可能是交换机或者错误
                _res = snmp.getLLDP(ip_address, comu_str)
        except:
            print("出现错误")
            exit(-1)
        else:
            res.update({
                snmp.getSysName(ip_address, comu_str): _res
            })
    return res
# getData()