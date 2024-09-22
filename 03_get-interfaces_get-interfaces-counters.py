from napalm import get_network_driver
import pprint

driver = get_network_driver('ios')
iol_01 = driver('192.168.100.8', 'gandalf', 'grey')
iol_01.open()

print('\nget_interfaces output:')
output = iol_01.get_interfaces()
pprint.pprint(output)

print('\nget_interfaces_counters output:')
output = iol_01.get_interfaces_counters()
pprint.pprint(output)

"""
get_interfaces output:
{'Ethernet0/0': {'description': '',
                 'is_enabled': True,
                 'is_up': True,
                 'last_flapped': -1.0,
                 'mac_address': 'AA:BB:CC:00:40:00',
                 'mtu': 1500,
                 'speed': 10.0},
 'Ethernet0/1': {'description': '',
                 'is_enabled': False,
                 'is_up': False,
                 'last_flapped': -1.0,
                 'mac_address': 'AA:BB:CC:00:40:10',
                 'mtu': 1500,
                 'speed': 10.0},
 'Ethernet0/2': {'description': '',
                 'is_enabled': False,
                 'is_up': False,
                 'last_flapped': -1.0,
                 'mac_address': 'AA:BB:CC:00:40:20',
                 'mtu': 1500,
                 'speed': 10.0},
 'Ethernet0/3': {'description': '',
                 'is_enabled': False,
                 'is_up': False,
                 'last_flapped': -1.0,
                 'mac_address': 'AA:BB:CC:00:40:30',
                 'mtu': 1500,
                 'speed': 10.0}}

get_interfaces_counters output:
{'Ethernet0/0': {'rx_broadcast_packets': 5272,
                 'rx_discards': 0,
                 'rx_errors': 0,
                 'rx_multicast_packets': 8,
                 'rx_octets': 760327,
                 'rx_unicast_packets': 5737,
                 'tx_broadcast_packets': -1,
                 'tx_discards': 0,
                 'tx_errors': 0,
                 'tx_multicast_packets': -1,
                 'tx_octets': 151628,
                 'tx_unicast_packets': 1152},
 'Ethernet0/1': {'rx_broadcast_packets': 0,
                 'rx_discards': 0,
                 'rx_errors': 0,
                 'rx_multicast_packets': 0,
                 'rx_octets': 0,
                 'rx_unicast_packets': 0,
                 'tx_broadcast_packets': -1,
                 'tx_discards': 0,
                 'tx_errors': 0,
                 'tx_multicast_packets': -1,
                 'tx_octets': 0,
                 'tx_unicast_packets': 0},
 'Ethernet0/2': {'rx_broadcast_packets': 0,
                 'rx_discards': 0,
                 'rx_errors': 0,
                 'rx_multicast_packets': 0,
                 'rx_octets': 0,
                 'rx_unicast_packets': 0,
                 'tx_broadcast_packets': -1,
                 'tx_discards': 0,
                 'tx_errors': 0,
                 'tx_multicast_packets': -1,
                 'tx_octets': 0,
                 'tx_unicast_packets': 0},
 'Ethernet0/3': {'rx_broadcast_packets': 0,
                 'rx_discards': 0,
                 'rx_errors': 0,
                 'rx_multicast_packets': 0,
                 'rx_octets': 0,
                 'rx_unicast_packets': 0,
                 'tx_broadcast_packets': -1,
                 'tx_discards': 0,
                 'tx_errors': 0,
                 'tx_multicast_packets': -1,
                 'tx_octets': 0,
                 'tx_unicast_packets': 0}}
"""
