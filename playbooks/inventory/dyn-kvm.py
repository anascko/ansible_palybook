#!/usr/bin/python
import sys
import libvirt

def our_inventory(group_name, name, ip):
    return {
        group_name: {
            'hosts': [name],
            'vars': {
                'ansible_ssh_host' : ip ,
                'ansible_user': 'root',
                'ansible_ssh_pass': 'r00tme'
            }
        }
    }

def inventory_kvm():
    conn = libvirt.open("qemu:///system")
    out = {}
    lease=conn.networkLookupByName("default").DHCPLeases()
    for myinventory in lease:
        # myinventory = lease.pop()
        ip = myinventory.get('ipaddr')
        name = myinventory.get('hostname')
        # import pdb; pdb.set_trace()
        if (name == 'jenkins'):
            group_name = 'master'
        else:
            group_name = 'slave'
        output = our_inventory(group_name, name, ip)
        out.update(output) 
    print (out)

if __name__ == '__main__':
    inventory_kvm()
