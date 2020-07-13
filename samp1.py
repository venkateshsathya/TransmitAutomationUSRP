import os
import string
import time
NumSeconds = 5
IQReceiveFileLocation = '/home/venkatesh/Desktop/USRPProject/DataCollect/'
IQReceiveFileName = 'AutomationTrial3'
IQReceiveFileInfo = IQReceiveFileLocation + IQReceiveFileName
pythonFile = 'ReceiveDataAutomated2.py'
Command1 = 'sudo python ' + pythonFile + ' ' + IQReceiveFileInfo + ' ' + str(NumSeconds)
print(Command1)
os.system(Command1)
#os.system('sudo python ReceiveDataAutomated2.py FileInfo NumSeconds')
print('Sleeping 5 seconds')
time.sleep(5)
print('Waking Up')
NumSeconds = 10
IQReceiveFileLocation = '/home/venkatesh/Desktop/USRPProject/DataCollect/'
IQReceiveFileName = 'AutomationTrial4'
IQReceiveFileInfo = IQReceiveFileLocation + IQReceiveFileName
Command2 = 'sudo python ' + pythonFile + ' ' + IQReceiveFileInfo + ' ' + str(NumSeconds)
os.system(Command2)
