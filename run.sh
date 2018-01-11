#!/bin/bash
sudo ansible-playbook playbooks/create_deploy_env.yml

for i in `virsh net-dhcp-leases default | grep -E 'slave|jenkins' | awk '{print $5}' | sed 's/\/24//'`; do ping -c10 -i3 $i; if [ $? -eq 0 ]; then echo "ENV is ready to run tasks"; else for k in 'slave' 'jenkins'; do virsh destroy $k; sleep 1s; virsh start $k; done fi; done

sudo chmod +x playbooks/inventory/dynamic-libvirt.py
sudo ansible-playbook main.yml -i playbooks/inventory/dynamic-libvirt.py
