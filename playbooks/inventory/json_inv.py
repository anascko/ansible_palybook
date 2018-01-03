#!/usr/bin/python
import sys
import libvirt
import json

def _prepare_inventory():
    hostvars = {}
    groups = {}
#    groups.update({'slave': []})
#    groups.update({'master': []})
    groups.update({'slave': {'hosts': []}})
    groups.update({'master': {'hosts': []}})
    return (groups, hostvars)

def main():

    vars={
         'ansible_user': 'root',
         'ansible_ssh_pass': 'r00tme'
    }
    (groups, hostvars) = _prepare_inventory()

    conn = libvirt.open("qemu:///system")
    lease=conn.networkLookupByName("default").DHCPLeases()
    for inser in lease:
        if inser['hostname'] in hostvars.keys():
            newhost=inser['hostname'] +'-'+ inser['mac']
            hostvars.update({newhost : {'ansible_ssh_host' : inser['ipaddr']}})
        else:
            hostvars.update({inser['hostname']: {'ansible_ssh_host' :inser['ipaddr']}})
        if inser['hostname'] != 'jenkins':
            hosts=inser['hostname']
#            print type(hosts)
            groups.update({'slave': hosts})
#            groups.update({'slave': inser['hostname']})
        else:
            groups.update({'master': inser['hostname']})
    hostvars.update(vars)
    inventory = {'_meta': {'hostvars': hostvars}}
    inventory.update(groups)
#    inventory.update(vars)
    print(json.dumps(inventory, indent=2))

if __name__ == '__main__':
    main()
