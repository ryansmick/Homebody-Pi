# Module to run arp command and parse output

import subprocess
import re

def scan():
    try:
        completed_process = subprocess.run(['arp', '-a'], stdout=subprocess.PIPE, universal_newlines=True)
    except subprocess.CalledProcessError as e:
        raise e

    hosts = {}
    for line in completed_process.stdout.split('\n'):
        host = parse_arp_line(line.strip())
        if host:
            hosts[host['ip']] = {'hostname': host['hostname'], 'MAC': host['MAC']}

    return hosts

def parse_arp_line(arp_line):
    pattern = re.compile("^([a-zA-Z0-9\?-]+) \(([0-9\.]+)\) at ([0-9A-Fa-f:]{17}) .*$")
    result = pattern.match(arp_line)
    if result:
        return {'ip': result.group(2), 'hostname': result.group(1), 'MAC': result.group(3)}
