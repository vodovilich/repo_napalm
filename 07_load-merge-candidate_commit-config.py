from napalm import get_network_driver
import pprint

driver = get_network_driver('ios')
iol_01 = driver('192.168.100.3', 'gandalf', 'grey')
iol_01.open()


iol_01.load_merge_candidate(filename='06.txt')
iol_01.commit_config()
iol_01.close()

"""
Works on Cisco IOS XE 17.03.03
Did not work on Cisco IOS 15.7(3)
"""
#FOR ONLY ONE COMMAND use CONFIG argument of load_merge_candidate method
# iol_01.load_merge_candidate(config='logging buffered 16501')
