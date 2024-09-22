import json
from napalm import get_network_driver
driver = get_network_driver('ios')
iol_01 = driver('192.168.100.13', 'gandalf', 'grey')
iol_01.open()

ios_output = iol_01.ping('8.8.8.8')
print(json.dumps(ios_output, indent=4))

"""
{'success': {'packet_loss': 0,
             'probes_sent': 5,
             'results': [{'ip_address': '8.8.8.8', 'rtt': 0.0},
                         {'ip_address': '8.8.8.8', 'rtt': 0.0},
                         {'ip_address': '8.8.8.8', 'rtt': 0.0},
                         {'ip_address': '8.8.8.8', 'rtt': 0.0},
                         {'ip_address': '8.8.8.8', 'rtt': 0.0}],
             'rtt_avg': 10.0,
             'rtt_max': 13.0,
             'rtt_min': 9.0,
             'rtt_stddev': 0.0}}
"""
