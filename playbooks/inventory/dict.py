#!/usr/bin/python
import sys
import libvirt

def _prepare_inventory(myinventory):
    hostvars = {}
    groups = {}
    hostvars.update({myinventory['hostname']: myinventory['ipaddr']})
#     if (group_name == 'master'):
    groups.update({'master': {'hosts': []}})
    groups.update({'slave': {'hosts': ["127.0.0.1"]}})
#    groups.update({group_name: {hosts.append(myinventory['hostname'])
#   groups['slave']['hosts'].append(k1['hostname'])
#     else:
#         groups['slave']['hosts'].append(myinventory['hostname'])
    return (groups, hostvars)

#                'vars': {
#                    'ansible_user': 'root',
#                    'ansible_ssh_pass': 'r00tme'}
#       }

def inventory_kvm():
    conn = libvirt.open("qemu:///system")
    out = {}
    lease=conn.networkLookupByName("default").DHCPLeases()
    for myinventory in lease:
        # myinventory = lease.pop()
        #ip = myinventory.get('ipaddr')
        name = myinventory.get('hostname')
        # import pdb; pdb.set_trace()
        if (name == 'jenkins'):
            group_name = 'master'
        else:
            group_name = 'slave'
        output=_prepare_inventory(myinventory)
        out.update(output) 
    print (out)

if __name__ == '__main__':
    _prepare_inventory()
