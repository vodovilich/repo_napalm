from napalm import get_network_driver
driver = get_network_driver('ios')
iol_01 = driver('192.168.100.13', 'gandalf', 'grey')
iol_01.open()

ios_output = iol_01.get_facts()
print(ios_output)