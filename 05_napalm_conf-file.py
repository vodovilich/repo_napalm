import json
from napalm import get_network_driver
driver = get_network_driver('ios')

#ISO-XE REQUIRED!!! won't work on IOS
iol_01 = driver('192.168.100.7', 'gandalf', 'grey')
iol_01.open()

print("Connecting to: " + "192.168.100.7")
iol_01.load_merge_candidate(config='logging buffered 16500')
iol_01.commit_config()
iol_01.close()