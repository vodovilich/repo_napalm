import json
from napalm import get_network_driver
driver = get_network_driver('ios')
iol_01 = driver('192.168.100.12', 'gandalf', 'grey')
iol_01.open()

print("Connecting to: " + "192.168.100.250")

iol_01.load_merge_candidate(filename='08_commands.cfg')

diffs = iol_01.compare_config()
if len(diffs) > 0:
    print(diffs)
    iol_01.commit_config()
else:
    print('No changes required')
    iol_01.discard_config()
iol_01.close()

"""
ERROR RETURNED on CSR1000v:
Connecting to: 192.168.100.7
Traceback (most recent call last):
  File "/home/gandalf/PythonDir/repo_napalm/08_list-conf.py", line 9, in <module>
    iol_01.load_merge_candidate(filename='07_commands.txt')
  File "/home/gandalf/PythonDir/repo_napalm/napalm-venv/lib/python3.9/site-packages/napalm/ios/ios.py", line 319, in load_merge_candidate
    return_status, msg = self._load_candidate_wrapper(
  File "/home/gandalf/PythonDir/repo_napalm/napalm-venv/lib/python3.9/site-packages/napalm/ios/ios.py", line 286, in _load_candidate_wrapper
    (return_status, msg) = self._scp_file(
  File "/home/gandalf/PythonDir/repo_napalm/napalm-venv/lib/python3.9/site-packages/napalm/ios/ios.py", line 735, in _scp_file
    return self._xfer_file(
  File "/home/gandalf/PythonDir/repo_napalm/napalm-venv/lib/python3.9/site-packages/napalm/ios/ios.py", line 791, in _xfer_file
    if not transfer.verify_space_available():
  File "/home/gandalf/PythonDir/repo_napalm/napalm-venv/lib/python3.9/site-packages/netmiko/scp_handler.py", line 213, in verify_space_available
    space_avail = self.remote_space_available(search_pattern=search_pattern)
  File "/home/gandalf/PythonDir/repo_napalm/napalm-venv/lib/python3.9/site-packages/netmiko/scp_handler.py", line 159, in remote_space_available
    raise ValueError(msg)
ValueError: pattern: (\d+) \w+ free not detected in output:

Directory of system:/

  758  drwx           0                    <no date>  cme
    2  -r--           0                    <no date>  default-running-config
    3  drwx           0                    <no date>  its
  105  dr-x           0                    <no date>  memory
    1  -rw-        1811                    <no date>  running-config
  104  dr-x           0                    <no date>  vfiles

No space information available
"""