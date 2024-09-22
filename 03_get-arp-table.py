from napalm import get_network_driver
import pprint

driver = get_network_driver('ios')
iol_01 = driver('192.168.100.8', 'gandalf', 'grey')
iol_01.open()


output = iol_01.get_arp_table()
pprint.pprint(output)

"""
[{'age': 0.0,
  'interface': 'Ethernet0/0',
  'ip': '192.168.100.1',
  'mac': '12:34:56:78:90:12'},
 {'age': -1.0,
  'interface': 'Ethernet0/0',
  'ip': '192.168.100.8',
  'mac': 'AA:BB:CC:00:40:00'},
 {'age': 23.0,
  'interface': 'Ethernet0/0',
  'ip': '192.168.100.11',
  'mac': '00:50:00:00:08:00'}]
"""
