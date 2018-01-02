#!/usr/bin/python
import sys
import libvirt

def inventory_kvm():
    conn=libvirt.open("qemu:///system")
    out=[]
    lease=conn.networkLookupByName("default").DHCPLeases()
    for i in lease:
        myinventory=lease.pop()
        ip = myinventory.get('ipaddr')
        name = myinventory.get('hostname')
        if name or ip:
            output = "{} ansible_ssh_host={} ansible_ssh_user=root ansible_ssh_password=r00tme".format(name, ip)
            out.append(output)
    print out

if __name__ == '__main__':
    inventory_kvm()
