#!/usr/bin/python
import sys
import libvirt
import json

def _prepare_inventory():
    hostvars = {}
    groups = {}
    groups.update({'slave': {'hosts': []}})
    groups.update({'master': {'hosts': []}})
    return (groups, hostvars)
def main():

    (groups, hostvars) = _prepare_inventory()
    group_name=''
    host={}
    param={}
    conn = libvirt.open("qemu:///system")
    lease=conn.networkLookupByName("default").DHCPLeases()
    for inser in lease:
        param={'ansible_ssh_host': inser['ipaddr'], 'ansible_ssh_user': 'root', 'ansible_ssh_pass': 'r00tme'}
        host={inser['hostname']: param }
        if inser['hostname'] == 'jenkins':
            group_name = 'master'
        else:
            group_name = 'slave'
        groups[group_name]['hosts'].append(inser['hostname'])
        hostvars.update(host)
    inventory = {'_meta': {'hostvars': hostvars}}
    inventory.update(groups)
    print(json.dumps(inventory, indent=2))

if __name__ == '__main__':
    main()
