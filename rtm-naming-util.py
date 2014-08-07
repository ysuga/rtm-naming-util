# 
#


import subprocess, sys

sp = subprocess.Popen(["ipconfig"], stdout=subprocess.PIPE)
sp.wait()

ipv4_key = 'IPv4 Address'
ipv4s = []
port = sys.argv[1]
for line in sp.stdout:
    if line.find(ipv4_key) < 0:
        continue
    ipv4s.append(line[line.find(':')+1:].strip())
    
for i, ipv4 in enumerate(ipv4s):
    #print ipv4,
    #if i != len(ipv4s)-1:
    print ' -ORBendPointPublish giop:tcp:%s:%s' % (ipv4, port)
        
