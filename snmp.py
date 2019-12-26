from snmp_cmds import snmpwalk


def getInfo(ip_address, config):
    res = snmpwalk(community='public',
                      ipaddress='192.168.27.218',
                      oid='1.3.6.1.2.1.4.20.1.4')

    for line in res:
        print(line[0], '     ', line[1])
    return
