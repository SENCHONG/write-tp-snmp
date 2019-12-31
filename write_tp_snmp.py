# -*-conding:utf-8-*-

import configparser
import json
import snmp


def snmpData():

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
            _res = snmp.getLLDP(ip_address, comu_str)
        except:
            print("出现错误")
            exit(-1)
        else:
            res.update({
                snmp.getSysName(ip_address, comu_str): _res
            })
    str_json = json.dumps(res, indent=2, ensure_ascii=False)
    print(str_json)

    return


snmpData()
