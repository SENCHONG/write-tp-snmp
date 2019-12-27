from snmp_cmds import snmpwalk


def getInfo(ip_address, config):
    res = snmpwalk(community='public',
                      ipaddress=ip_address,
                      oid="1.3.6.1.4.1.3320.127.1.4")

    for line in res:
        print(line[0], '     ', line[1])
    return

# interfaces_table_named_oid = [
#     ('IF-MIB', 'ifDescr'),
#     ('IF-MIB', 'ifType'),
#     ('IF-MIB', 'ifMtu'),
#     ('IF-MIB', 'ifSpeed'),
#     ('IF-MIB', 'ifPhysAddress'),
#     ('IF-MIB', 'ifAdminStatus'),
#     ('IF-MIB', 'ifOperStatus'),
#     ('IF-MIB', 'ifHCInOctets'),
#     ('IF-MIB', 'ifHCOutOctets'),
#     ('IF-MIB', 'ifHighSpeed')
# ]

# lldp_table_named_oid = [
#     ('LLDP-MIB', 'lldpRemSysName'),
#     ('LLDP-MIB', 'lldpRemSysDesc'),
#     ('LLDP-MIB', 'lldpRemPortId'),
#     ('LLDP-MIB', 'lldpRemPortDesc')
# ]'SNMPv2-MIB', 'sysName'