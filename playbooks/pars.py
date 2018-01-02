#!/usr/bin/python
import sys
import re


def parse_output():
    vms_addresses = sys.argv[1]
    f = open('/home/ovosh/ansible/ou.txt', 'a')
    #f.write(vms_addresses)

    lst = vms_addresses.split('\n')
    out = []
    for i in lst:
        f.write('\n\n')
        f.write(i)
    #for i in lst:
    #    ip = re.findall( r'[0-9]+(?:\.[0-9]+){3}', i )
    #    name = re.findall( r'jenkins', i )
    #        if name or ip:
    #            output = "{} ansible_ssh_host={} ansible_ssh_user=root ansible_ssh_password=r00tme".format(name, ip)
    #            out.append(output)

    #return '\n'.join(out)

if __name__ == '__main__':
    parse_output()
