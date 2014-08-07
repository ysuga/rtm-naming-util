#!/usr/bin/python

from __future__ import print_function

import re
import subprocess
import sys

def get_win32_ips():
    # Only works in Python 2.7 or greater
    #cmd_output = subprocess.check_output(["ipconfig"])
    sp = subprocess.Popen(["ipconfig"], stdout=subprocess.PIPE,
            universal_newlines=True)
    sp.wait()
    matches = re.finditer(r'^\w.*?:.*?\s+IPv4 Address[\. ]+: (?P<ip>(?:\d{1,3}\.){3}\d{1,3})',
            ''.join(sp.stdout.readlines()), flags=re.DOTALL | re.MULTILINE)
    return [m.group('ip') for m in matches]


def get_unix_ips():
    # Only works in Python 2.7 or greater
    #cmd_output = subprocess.check_output(["ifconfig"])
    sp = subprocess.Popen(["ifconfig"], stdout=subprocess.PIPE,
            universal_newlines=True)
    sp.wait()
    matches = re.finditer(r'^\w.*?:.*?\s+inet (?P<ip>(?:\d{1,3}\.){3}\d{1,3})',
            ''.join(sp.stdout.readlines()), flags=re.DOTALL | re.MULTILINE)
    return [m.group('ip') for m in matches]


if len(sys.argv) > 1:
    port = ':' + sys.argv[1]
else:
    port = ''

if sys.platform == 'win32' or sys.platform == 'cygwin':
    ips = get_win32_ips()
else:
    ips = get_unix_ips()

output = ''
for ip in ips:
    # port already contains the : needed between it and the IP, or is an empty
    # string if no port specified
    output += ' -ORBendPointPublish giop:tcp:{ip}{port}'.format(ip=ip, port=port)
print(output)


# vim: tw=79

