import json
from napalm import get_network_driver

nbr_list = ['192.168.100.12',
            '192.168.100.13'
            ]


for bgp_nbr in nbr_list:
    print("\n\nConnecting to " + str(bgp_nbr))
    driver = get_network_driver('ios')
    ios = driver(bgp_nbr, 'gandalf', 'grey')
    ios.open()

    bgp_nbrs = ios.get_bgp_neighbors()
    print(json.dumps(bgp_nbrs, indent=4))

    ios.close()