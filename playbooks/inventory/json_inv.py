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
    varss = {
        'ansible_user': 'root',
        'ansible_ssh_pass': 'r00tme'
            }
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
#        groups[group_name]['hosts'].append(host['name'])
#        hostvars.update({host['name']: row['ipaddr']})
        hostvars.update({row['ipaddr']: host['name']})
    inventory = {'_meta': {'hostsvars': hostvars, 'vars': varss}}
    inventory.update(groups)
#    inventory.update({'vars' : varss})
#    print(json.dumps(inventory, indent=2))
    print (inventory)

if __name__ == '__main__':
    main()
