#-*-conding:utf-8-*-

import configparser
import json
import snmp

def init():
    config = configparser.ConfigParser()
    config.read('config.ini')
    config.sections()
    if "DEVICES" not in config or "DEFAULT" not in config:
        print("错误：缺乏配置文件")
        exit(1)
    ip_address_list = json.loads(config["DEVICES"]["address"])

    for ip_address in ip_address_list:
        ip_address = ip_address.replace("\n", '')
        start(ip_address, config)
    return

def start(ip_address, config):
    # try:
    #     snmp_host_name = 
    snmp.getInfo(ip_address, config)
    return


if __name__ == "__main__":
    init()