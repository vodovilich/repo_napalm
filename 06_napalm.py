import json
from napalm import get_network_driver
driver = get_network_driver('ios')
iol_01 = driver('192.168.100.12', 'gandalf', 'grey')
iol_01.open()

print("Connecting to: " + "192.168.100.12")

iol_01.load_merge_candidate(filename='05_commands.cfg')

diffs = iol_01.compare_config()
if len(diffs) > 0:
    print(diffs)
    iol_01.commit_config()
else:
    print('No changes required')
    iol_01.discard_config()
iol_01.close()