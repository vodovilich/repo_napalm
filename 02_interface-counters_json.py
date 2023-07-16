import json
from napalm import get_network_driver
driver = get_network_driver('ios')
iol_01 = driver('192.168.100.13', 'gandalf', 'grey')
iol_01.open()

ios_output = iol_01.get_interfaces_counters()
print(json.dumps(ios_output, indent=4, sort_keys=True))

ios_output = iol_01.get_interfaces()
print(json.dumps(ios_output, indent=4))
