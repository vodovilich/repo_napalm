import json
from napalm import get_network_driver
driver = get_network_driver('ios')
iol_01 = driver('192.168.100.13', 'gandalf', 'grey')
iol_01.open()

ios_output = iol_01.get_facts()
print (json.dumps(ios_output, indent=4))

"""
{'fqdn': 'iol-157-01.atffk.hui',
 'hostname': 'iol-157-01',
 'interface_list': ['Ethernet0/0', 'Ethernet0/1', 'Ethernet0/2', 'Ethernet0/3'],
 'model': 'Unknown',
 'os_version': 'Linux Software (I86BI_LINUX-ADVENTERPRISEK9-M), Version '
               '15.7(3)M0.1, DEVELOPMENT TEST SOFTWARE',
 'serial_number': '12345678',
 'uptime': 2880.0,
 'vendor': 'Cisco'}
 """
