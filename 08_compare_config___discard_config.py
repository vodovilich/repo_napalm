from napalm import get_network_driver
import pprint

driver = get_network_driver('ios')
iol_01 = driver('192.168.100.3', 'gandalf', 'grey')
iol_01.open()

iol_01.load_merge_candidate(filename='07.txt')
diff = iol_01.compare_config()
print(type(diff))

if len(diff) > 0:
    print(diff)
    iol_01.commit_config()
else:
    print('No changes required.')
    iol_01.discard_config()
    print(diff)
iol_01.close()


"""
==========WIRESHARK==========
Only SSH:22 interaction, no NETCONF

==========DO NOT FORGET ABOUT NUMBERS IN ACL LINES==========
DIFF
+ip access-list extended rfc1918-in-acl
+ deny ip 10.0.0.0 0.255.255.255 any
+ deny ip 172.16.0.0 0.15.255.255 any
+ deny ip 192.168.0.0 0.0.255.255 any
+ permit ip any any
returned if NO STRING NUMBERS in 07.txt , because in config THERE ARE STRING NUMBERS

==========CREATED FILES==========
if NO CHANGES - creates:
csr1000v-01#dir | i config
24      -rw-             7133  Sep 22 2024 16:53:41 +00:00  candidate_config.txt
22      -rw-                0  Sep 22 2024 16:53:41 +00:00  merge_config.txt

if there ARE CHANGES - creates:
24      -rw-             7133  Sep 22 2024 16:54:50 +00:00  rollback_config.txt
22      -rw-              268  Sep 22 2024 16:54:49 +00:00  merge_config.txt


==========Cisco console logs==========:
*Sep 22 16:23:09.466: %SEC_LOGIN-5-LOGIN_SUCCESS: Login Success [user: gandalf] [Source: 192.168.100.11] [localport: 22] at 16:23:09 UTC Sun Sep 22 2024
*Sep 22 16:23:10.484: %SEC_LOGIN-5-LOGIN_SUCCESS: Login Success [user: gandalf] [Source: 192.168.100.11] [localport: 22] at 16:23:10 UTC Sun Sep 22 2024
*Sep 22 16:23:11.270: %SYS-5-CONFIG_I: Configured from console by gandalf on vty0 (192.168.100.11)
*Sep 22 16:23:11.907: %SYS-5-CONFIG_P: Configured programmatically by process SSH Process from console as gandalf on vty0 (192.168.100.11)
*Sep 22 16:23:11.907: %PARSER-4-BADCFG: Unexpected end of configuration file.
*Sep 22 16:23:11.908: %SYS-5-CONFIG_C: Running-config file is Modified
*Sep 22 16:23:11.911: %DMI-5-SYNC_NEEDED: R0/0: dmiauthd: Configuration change requiring running configuration sync detected - ''. The running configuration will be synchronized  to the NETCONF running data store.
*Sep 22 16:23:13.027: %SYS-5-CONFIG_I: Configured from console by gandalf on vty0 (192.168.100.11)
*Sep 22 16:23:13.064: %SYS-6-LOGOUT: User gandalf has exited tty session 1(192.168.100.11)
csr1000v-01#
csr1000v-01#
*Sep 22 16:23:14.995: %DMI-5-SYNC_COMPLETE: R0/0: dmiauthd: The running configuration has been synchronized to the NETCONF running data store.

==========show history:==========
*Sep 22 16:23:09.466: %SEC_LOGIN-5-LOGIN_SUCCESS: Login Success [user: gandalf] [Source: 192.168.100.11] [localport: 22] at 16:23:09 UTC Sun Sep 22 2024
CMD: 'terminal width 511' 16:23:09 UTC Sun Sep 22 2024
CMD: 'terminal length 0' 16:23:09 UTC Sun Sep 22 2024
CMD: 'dir' 16:23:09 UTC Sun Sep 22 2024

CMD: 'dir bootflash:' 16:23:09 UTC Sun Sep 22 2024
*Sep 22 16:23:10.484: %SEC_LOGIN-5-LOGIN_SUCCESS: Login Success [user: gandalf] [Source: 192.168.100.11] [localport: 22] at 16:23:10 UTC Sun Sep 22 2024
CMD: 'dir bootflash:/merge_config.txt' 16:23:10 UTC Sun Sep 22 2024
CMD: 'verify /md5 bootflash:/merge_config.txt' 16:23:10 UTC Sun Sep 22 2024
CMD: 'show archive config incremental-diffs bootflash:/merge_config.txt ignorecase' 16:23:10 UTC Sun Sep 22 2024
CMD: 'show archive' 16:23:11 UTC Sun Sep 22 2024
CMD: 'configure terminal' 16:23:11 UTC Sun Sep 22 2024
CMD: 'file prompt quiet' 16:23:11 UTC Sun Sep 22 2024
CMD: 'end' 16:23:11 UTC Sun Sep 22 2024
*Sep 22 16:23:11.270: %SYS-5-CONFIG_I: Configured from console by gandalf on vty0 (192.168.100.11)
CMD: 'copy running-config bootflash:/rollback_config.txt' 16:23:11 UTC Sun Sep 22 2024
CMD: 'dir bootflash:/merge_config.txt' 16:23:11 UTC Sun Sep 22 2024
CMD: 'copy bootflash:/merge_config.txt running-config' 16:23:11 UTC Sun Sep 22 2024
CMD: 'logging buffered 16504' 16:23:11 UTC Sun Sep 22 2024
CMD: 'ip access-list extended rfc1918-in-acl' 16:23:11 UTC Sun Sep 22 2024
CMD: ' deny ip 10.0.0.0 0.255.255.255 any' 16:23:11 UTC Sun Sep 22 2024
CMD: ' deny ip 172.16.0.0 0.15.255.255 any' 16:23:11 UTC Sun Sep 22 2024

CMD: ' deny ip 192.168.0.0 0.0.255.255 any' 16:23:11 UTC Sun Sep 22 2024
CMD: ' permit ip any any ' 16:23:11 UTC Sun Sep 22 2024
*Sep 22 16:23:11.907: %SYS-5-CONFIG_P: Configured programmatically by process SSH Process from console as gandalf on vty0 (192.168.100.11)
*Sep 22 16:23:11.907: %PARSER-4-BADCFG: Unexpected end of configuration file.

*Sep 22 16:23:11.908: %SYS-5-CONFIG_C: Running-config file is Modified
CMD: 'show running-config brief' 16:23:11 UTC Sun Sep 22 2024
CMD: 'write mem' 16:23:12 UTC Sun Sep 22 2024
*Sep 22 16:23:11.911: %DMI-5-SYNC_NEEDED: R0/0: dmiauthd: Configuration change requiring running configuration sync detected - ''. The running configuration will be synchronized  to the NETCONF running data store.
CMD: 'configure terminal' 16:23:12 UTC Sun Sep 22 2024
CMD: 'no file prompt quiet' 16:23:12 UTC Sun Sep 22 2024
CMD: 'end' 16:23:13 UTC Sun Sep 22 2024
*Sep 22 16:23:13.027: %SYS-5-CONFIG_I: Configured from console by gandalf on vty0 (192.168.100.11)
CMD: 'exit' 16:23:13 UTC Sun Sep 22 2024
*Sep 22 16:23:13.064: %SYS-6-LOGOUT: User gandalf has exited tty session 1(192.168.100.11)
*Sep 22 16:23:14.995: %DMI-5-SYNC_COMPLETE: R0/0: dmiauthd: The running configuration has been synchronized to the NETCONF running data store.
"""
