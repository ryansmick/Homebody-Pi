# Python module to run nmap scan for host discovery

import subprocess
import re

# Function to scan the network using nmap
def scan(ip_range):
    try:
        completed_process = subprocess.run(['nmap', '-oG', '-', '-sn', ip_range.get_string_representation()], stdout=subprocess.PIPE, universal_newlines=True)
    except subprocess.CalledProcessError as e:
        raise e

    hosts = set()
    for line in completed_process.stdout.split('\n'):
        host = parse_nmap_line(line.strip())
        if host:
            hosts.add(host)
    return hosts

def parse_nmap_line(line):
    pattern = re.compile("^Host: ([0-9\.]+) .*$")
    result = pattern.match(line)
    if result:
        return result.group(1)
