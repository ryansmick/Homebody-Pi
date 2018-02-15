import math

class IPv4Addr:
    def __init__(self, addr):
        self.addr = 0

        # If the address is a four part string, parse it to a single 32-bit integer
        if type(addr) is str:
                for val in addr.split('.'):
                    try:
                        val = int(val)
                    except ValueError:
                        raise ValueError('Each value in ip must be an integer between 0 and 255 inclusive')

                    if val > 255 or val < 0:
                        raise ValueError('addr is not possible. Contains values below 0 or above 255.')
                    self.addr = self.addr << 8
                    self.addr = self.addr | val
                return
        
        # If the addr is an integer, make sure it's values are valid and store it
        elif type(addr) is int:
            if self.addr < 0 or self.addr > (math.pow(2, 32)-1):
                raise ValueError('addr is less than 0 or greater than the max value of a 32-bit integer')
            self.addr = addr

    # Return the ip in the format 255.255.255.255
    def get_string_representation(self):
        addr = self.addr
        addr_array = []
        while addr != 0:
            addr_array.append(str(addr & 255))
            addr = addr >> 8

        addr_array.reverse()
        return '.'.join(addr_array)

    # Return a 32-bit integer representing the ip
    def get_numerical_representation(self):
        return self.addr

    # Return an IPv4Addr object representing the bitwise and of two IPv4Addr objects
    def bitwise_and(self, other_ip):
        try:
            return IPv4Addr(self.addr & other_ip.addr)
        except ValueError as e:
            raise e

    # Function to get the number of starting ones in the binary representation of the ip address
    def get_num_starting_ones(self):
        addr = self.addr
        counter = 0
        while addr % 2 == 0:
            counter += 1
            addr = addr >> 1
        return 32 - counter

# Class to represent a range of IP addresses in CIDR notation
class IPv4CIDR:
    # Constructor: accepts an IPv4Addr object and an integer representing a prefix length
    def __init__(self, ipv4, prefix_length):
        if ipv4.__class__.__name__ != 'IPv4Addr':
            raise ValueError('First argument to constructor must be of type IPv4Addr')
        if prefix_length > 32 or prefix_length < 0:
            raise ValueError('prefix_length must be between 0 and 32 inclusive')
        self.addr = ipv4
        self.prefix_length = prefix_length

    def get_string_representation(self):
        return self.addr.get_string_representation() + '/' + str(self.prefix_length)
