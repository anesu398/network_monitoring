from pysnmp.hlapi import *

def get_snmp_data(ip_address, community, oid):
    error_indication, error_status, error_index, var_binds = next(
        getCmd(SnmpEngine(),
               CommunityData(community),
               UdpTransportTarget((ip_address, 161)),
               ContextData(),
               ObjectType(ObjectIdentity(oid)))
    )

    if error_indication:
        print(error_indication)
        return None
    elif error_status:
        print('%s at %s' % (error_status.prettyPrint(),
                            error_index and var_binds[int(error_index) - 1] or '?'))
        return None
    else:
        return var_binds[0][1].prettyPrint()

# Example usage
data = get_snmp_data('192.168.1.1', 'public', '1.3.6.1.2.1.1.1.0')
print("System Description:", data)
