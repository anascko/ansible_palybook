#!/usr/bin/python
import sys
import libvirt
import json

def _prepare_inventory():
    hostvars = {}
    groups = {}
    groups.update({'slave': {'hosts': [],'vars': {'ansible_user': 'root', 'ansible_ssh_pass': 'r00tme'}}})
    groups.update({'master': {'hosts': [], 'vars': {'ansible_user': 'root', 'ansible_ssh_pass': 'r00tme'}}})
    return (groups, hostvars)


def main():
    (groups, hostvars) = _prepare_inventory()
    group_name=''
    host={}
    conn = libvirt.open("qemu:///system")
    lease=conn.networkLookupByName("default").DHCPLeases()
    for row in lease:
        host['name'] = row['hostname']
        if row['hostname'] == 'jenkins':
            group_name = 'master'
        else:
            group_name = 'slave'
        groups[group_name]['hosts'].append(row['ipaddr'])
        hostvars.update({row['ipaddr']: host['name']})
    inventory = {'_meta': {'hostsvars': hostvars}}
    inventory.update(groups)
    print json.dumps(inventory, indent=2)

if __name__ == '__main__':
    main()
