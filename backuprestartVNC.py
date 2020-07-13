from subprocess import check_output
def get_pid(name):
    return check_output(["pidof",name])

print('VNC PID is: ' + get_pid('./x11vnc'))
vncPID = get_pid('./x11vnc')
import os
vncKillCmd = 'kill -9 ' + str(vncPID)
os.system(vncKillCmd)
print('./x11vnc process killed')
print('Printing the exiting process of x11vnc')
print('/bin/ps -ef|/bin/grep x11vnc')
print('Restarting VNC Thread')
os.system('/home/venkatesh/x11vnc-0.9.14/x11vnc/x11vnc')
print('/bin/ps -ef|/bin/grep x11vnc')
