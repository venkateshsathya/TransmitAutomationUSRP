import os

checkVNCThread = '/bin/ps -ef|/bin/grep ./x11vnc > /tmp/vnclogs1.txt'
os.system(checkVNCThread)
with open('/tmp/vnclogs1.txt') as f:
    if './x11vnc' in f.read():
        print("VNC Seems to be running - location is /home/venkatesh/x11vnc-0.9.14/x11vnc/x11vnc ")
    else:
        print('VNC seems to have died - restarting it')
        os.system('/home/venkatesh/x11vnc-0.9.14/x11vnc/x11vnc')
