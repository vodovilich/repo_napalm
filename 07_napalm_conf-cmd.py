import json
from napalm import get_network_driver
driver = get_network_driver('ios')

#ISO-XE REQUIRED!!! won't work on IOS


iplist = ['192.168.100.7']
for ip_host in iplist:
    print("Connecting to: " + str(ip_host))
    iol_01 = driver(ip_host, 'gandalf', 'grey')
    iol_01.open()
    iol_01.load_merge_candidate(filename='07_commands.txt')
    iol_01.commit_config()
    iol_01.close()
    
    
#FOR ONLY ONE COMMAND use CONFIG argument of load_merge_candidate method
# iol_01.load_merge_candidate(config='logging buffered 16501')