from ip_addr import IPv4Addr, IPv4CIDR
import network_utils
import time, arp, nmap, ping
import sys

sleep_time = 240 # Time to wait between scans (in seconds)

net_iface_name = input('Please enter the network interface name: ')

print('Retrieving device ip and subnet mask...')
device_ip = network_utils.get_interface_ip(net_iface_name)
subnet_mask = network_utils.get_interface_subnet_mask(net_iface_name)

print('Calculating subnet ip and subnet prefix...')
subnet_ip = device_ip.bitwise_and(subnet_mask)
mask_length = subnet_mask.get_num_starting_ones()

host_range = IPv4CIDR(subnet_ip, mask_length)
print('Host Range: {}'.format(host_range.get_string_representation()))

# Get hostnames and ip addresses for devices on network
print('Beginning scan loop...')
while True:
    print('Scanning subnet...')
   
    nmap_devices = nmap.scan(host_range)
    arp_devices = arp.scan()

    for device in arp_devices.keys() - nmap_devices:
        print('Device missing from nmap scan: {}'.format(device))
        if not ping.host_is_up(IPv4Addr(device)):
            del arp_devices[device]
            print('Device {} not found'.format(device))
        else:
            print('Found device {}'.format(device))

    print('Found {} host(s) on subnet:'.format(len(arp_devices)))
    for ip in arp_devices:
        print('\t{}: {} {}'.format(ip, arp_devices[ip]['hostname'] if arp_devices[ip]['hostname'] else '(unknown hostname)', arp_devices[ip]['MAC']))

    for i in range(sleep_time, 0, -1):
        sys.stdout.write('\rScan will run again in {} seconds...'.format(i))
        sys.stdout.flush()
        time.sleep(1)
