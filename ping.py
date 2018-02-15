# Module to ping a specific ip

import subprocess

def host_is_up(ip_addr):
    try:
        completed_process = subprocess.run(['ping', '-c', '10', '-t', '5', ip_addr.get_string_representation()], stdout=subprocess.PIPE)
    except subprocess.CalledProcessError as e:
        raise e

    return True if completed_process.returncode == 0 else False
