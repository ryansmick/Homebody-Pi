import netifaces
from ip_addr import IPv4Addr

# Returns list of available network interfaces
def get_interfaces_list():
    return netifaces.interfaces()

# Returns a dictionary containing the interface ip and subnet mask
def get_interface_data(interface):
    if interface not in get_interfaces_list():
        raise ValueError('Interface ' + interface + ' is not available')

    return netifaces.ifaddresses(interface)[netifaces.AF_INET][0]

# Returns the ip address of the given network interface
def get_interface_ip(interface):
    try:
        return IPv4Addr(get_interface_data(interface)['addr'])
    except ValueError as e:
        raise e
    except KeyError:
        raise ValueError('No data could be gathered for interface ' + interface)

def get_interface_subnet_mask(interface):
    try:
        return IPv4Addr(get_interface_data(interface)['netmask'])
    except ValueError as e:
        raise e
    except KeyError:
        raise ValueError('No data could be gathered for interface ' + interface)
