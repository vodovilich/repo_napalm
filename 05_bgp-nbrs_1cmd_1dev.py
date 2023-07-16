import json
from napalm import get_network_driver
driver = get_network_driver('ios')
ios = driver('192.168.100.12', 'gandalf', 'grey')
ios.open()

bgp_nbrs = ios.get_bgp_neighbors_detail()
print(json.dumps(bgp_nbrs, indent=4))

ios.close()

ios = driver('192.168.100.12', 'gandalf', 'grey')
ios.open()
bgp_nbrs = ios.get_bgp_neighbors()
print(json.dumps(bgp_nbrs, indent=4))
ios.close()

"""
OUTPUT OF get_bgp_neighbors:
{
    "global": {
        "router_id": "192.168.255.20",
        "peers": {
            "192.168.100.7": {
                "local_as": 65001,
                "remote_as": 65001,
                "remote_id": "192.168.255.30",
                "is_up": true,
                "is_enabled": true,
                "description": "",
                "uptime": 7170,
                "address_family": {
                    "ipv4 unicast": {
                        "received_prefixes": 1,
                        "accepted_prefixes": 1,
                        "sent_prefixes": 1
                    }
                }
            },


OUTPUT OF get_bgp_neighbors_detail:
    "global": {
        "65001": [
            {
                "up": true,
                "local_as": 65001,
                "remote_as": 65001,
                "router_id": "192.168.255.30",
                "local_address": "192.168.100.12",
                "local_address_configured": true,
                "local_port": 17022,
                "routing_table": "global",
                "remote_address": "192.168.100.7",
                "remote_port": 179,
                "multihop": false,
                "multipath": false,
                "remove_private_as": false,
                "import_policy": "",
                "export_policy": "",
                "input_messages": 124,
                "output_messages": 127,
                "input_updates": 2,
                "output_updates": 3,
                "messages_queued_out": 0,
                "connection_state": "Established",
                "previous_connection_state": "",
                "last_event": "",
                "suppress_4byte_as": false,
                "local_as_prepend": false,
                "holdtime": 180,
                "configured_holdtime": 0,
                "keepalive": 60,
                "configured_keepalive": 0,
                "active_prefix_count": 1,
                "received_prefix_count": 1,
                "accepted_prefix_count": 1,
                "suppressed_prefix_count": 0,
                "advertised_prefix_count": 1,
                "flap_count": 0
            },
"""