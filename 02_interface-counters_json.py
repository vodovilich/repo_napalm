import json
from napalm import get_network_driver
driver = get_network_driver('ios')
iol_01 = driver('192.168.100.13', 'gandalf', 'grey')
iol_01.open()

ios_output = iol_01.get_interfaces_counters()
print(json.dumps(ios_output, indent=4, sort_keys=True))

ios_output = iol_01.get_interfaces()
print(json.dumps(ios_output, indent=4))

"""
{
    "Ethernet0/0": {
        "rx_broadcast_packets": 1969,
        "rx_discards": 0,
        "rx_errors": 0,
        "rx_multicast_packets": 8,
        "rx_octets": 231102,
        "rx_unicast_packets": 2519,
        "tx_broadcast_packets": -1,
        "tx_discards": 0,
        "tx_errors": 0,
        "tx_multicast_packets": -1,
        "tx_octets": 164978,
        "tx_unicast_packets": 1340
    },
"""