import os
import string
import time
import string
from datetime import datetime


DataCollectAdditionalDetails = ''
ModulationTypes = ["BPSK", "QPSK", "8PSK", \
  "16QAM", "64QAM", "PAM4", "GFSK", "CPFSK", \
  "BFM", "DSBAM", "SSBAM"]

IntialSleep = 35
#IntialSleep = 3
DurationDataCollect = 45
#DurationDataCollect = 5
SleepAfterEachTest = 85
#SleepAfterEachTest = 10

#Note that the sleep and test duration numbers are picked carefully to sync with the transmit
#The duration of collect logic is as follows: 10^4*1024 samples have to be captured at a rate of
# 250k per second. Thus it take marginally over 40 seconds to capture - we set that number to 45. 
#We pass that value to the head block which stops the test after those many samples have passed through it. 

# The number 35 of initial sleep is so that we capture data somewhere in the middle of the 20 seconds
#the TX is playing. This way we can absorb a lot of drift that can happen in both directions - due to mismatch in 
#timing in ecah iteration ebtween TX and R that nmy accumulate.

#Note that we have also accounted for the time taken to start the USRP and stop. 
print('Sleeping for ', IntialSleep, ' seconds')
time.sleep(IntialSleep)
for value in ModulationTypes:
		now = datetime.now()
		date_time = now.strftime("%m_%d_%Y_%H_%M")
		IQReceiveFileLocation = '/home/venkatesh/Desktop/USRPProject/DataCollect/'
		IQReceiveFileName = date_time + '_' + value + DataCollectAdditionalDetails
		IQReceiveFileInfo = IQReceiveFileLocation + IQReceiveFileName
		# We have now created files with the appropriate mod type appended with the data and time
		
		# We now need to add correct values of time of collect and wait between each collect.
		# We collect as many time as there are modulation types.
		# We collect data for 40 seconds and sleep for 85 seconds after that.
		# We repeat this for all mod types. The sleep after last mod type is not necessary, doesn't hurt as well 
		
		pythonFileLocation = '/home/venkatesh/Desktop/USRPProject/FlowGraphs/'
		pythonFile = pythonFileLocation + 'ReceiveUsrpControl.py'
		commandLine = 'sudo python ' + pythonFile + ' ' + IQReceiveFileInfo + ' ' + str(DurationDataCollect)
		print('What we issue in command line is: ', commandLine)
		print('We are collecting data for', )
		os.system(commandLine)
		print('Sleeping for ', SleepAfterEachTest, ' seconds')
		time.sleep(SleepAfterEachTest)
		print('Waking Up after sleep')	

print('CollectComplete')
  #IQReceiveFileInfo = 
#NumSeconds = 5
#IQReceiveFileLocation = '/home/venkatesh/Desktop/USRPProject/DataCollect/'
#IQReceiveFileName = 'AutomationTrial3'
#IQReceiveFileInfo = IQReceiveFileLocation + IQReceiveFileName
#pythonFile = 'ReceiveDataAutomated2.py'
#Command1 = 'sudo python ' + pythonFile + ' ' + IQReceiveFileInfo + ' ' + str(NumSeconds)
#print(Command1)
#os.system(Command1)
#os.system('sudo python ReceiveDataAutomated2.py FileInfo NumSeconds')
#print('Sleeping 5 seconds')
#time.sleep(5)
#print('Waking Up')
#NumSeconds = 10
#IQReceiveFileLocation = '/home/venkatesh/Desktop/USRPProject/DataCollect/'
#IQReceiveFileName = 'AutomationTrial4'
#IQReceiveFileInfo = IQReceiveFileLocation + IQReceiveFileName
#Command2 = 'sudo python ' + pythonFile + ' ' + IQReceiveFileInfo + ' ' + str(NumSeconds)
#os.system(Command2)
