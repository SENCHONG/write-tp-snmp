from snmp_cmds import snmpwalk
import json

# 获取设备的名称


def getSysName(ip_address, comu_str):
    res = snmpwalk(community=comu_str,
                   ipaddress=ip_address,
                   oid="SNMPv2-MIB:sysName")
    return res[0][1]

def sysDescr(ip_address, comu_str):
    res = snmpwalk(community=comu_str,
                   ipaddress=ip_address,
                   oid="SNMPv2-MIB:sysDescr")
    return res[0][1]

# 获取LLDP
def getLLDP(ip_address, comu_str):
    res = []
    loc_desc = {}
    i = 0
    loc_name = getSysName(ip_address, comu_str)

    # 邻居接口名称
    lldpRemPortDesc_res = snmpwalk(community=comu_str,
                                   ipaddress=ip_address,
                                   oid="LLDP-MIB:lldpRemPortDesc")
    # 邻居系统名称
    lldpRemSysName_res = snmpwalk(community=comu_str,
                                  ipaddress=ip_address,
                                  oid="LLDP-MIB:lldpRemSysName")
    # 本机接口名称
    ifDescr_res = snmpwalk(community=comu_str,
                           ipaddress=ip_address,
                           oid="IF-MIB:ifDescr")
    for line in ifDescr_res:
        loc_indexs = line[0].split('.')
        loc_desc.update(
            {
                loc_indexs[-1]: line[1]
            }
        )
    while i < len(lldpRemPortDesc_res):
        lldpRemPortDesc_indexs = lldpRemPortDesc_res[i][0].split('.')
        res.append(
            {
                "local_interface_index": lldpRemPortDesc_indexs[-2],
                "local_sysName": loc_name,
                "local_interface": loc_desc[str(lldpRemPortDesc_indexs[-2])],
                "remote_interface": lldpRemPortDesc_res[i][1].replace(" Interface", ""),
                "remote_sysName": lldpRemSysName_res[i][1],
                "remote_interface_index": lldpRemPortDesc_indexs[-1]
            }

        )
        i += 1
    # str_json = json.dumps(res, indent=2, ensure_ascii=False)
    # print(res)
    return res



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
#     ('LLDP-MIB', 'lldpRemPortId'),lldpLocPortId
#     ('LLDP-MIB', 'lldpRemPortDesc')
# ]'SNMPv2-MIB', 'sysName'
