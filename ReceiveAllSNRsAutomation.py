import os
import string
import time
import string
from datetime import datetime
import os.path
from os import path
import sys
import datetime
###############################################################
#################   STATE DIAGRAM  ############################
###############################################################
# Wait for dummy file receive (indirect way of synchronizing the TX and RX controlling laptops and also pasisng on 
# info about the type of signal being transmitted). Once dummy file received, check signal being transmitted by reading file and immediately delete the file, then wait for 7 seconds,
# receive file for 15 seconds. We are reading for 15 seconds because the waveform played is about 10 seconds long (repeatedly played) plus additional 5 secs
# buffer. 

DataCollectAdditionalDetails = ''
ModulationTypes = ["BPSK", "QPSK", "8PSK", \
  "16QAM", "64QAM", "PAM4", "GFSK", "CPFSK", \
  "BFM", "DSBAM", "SSBAM"]



#IntialSleep = 35
#IntialSleep = 3
DurationDataCollect = 50
SleepAfterEachTest = 20
waitBeforeprogramexit = 400 # Wait time for indication that signal is transmitted. If we wait longer than this, program assumes transmission is complete and exits.
waiteachiterationFilecheck = 0.1
IQReceiveFileLocation = '/home/venkatesh/Desktop/USRPProject/DataCollect/IQSamples/Receive/Sep11thCollectPaper/AWGN/'
pythonFileLocation = '/home/venkatesh/Desktop/USRPProject/FlowGraphs/'
pythonFile = pythonFileLocation + 'ReceiveUsrpControlAllSNRs.py'

#Note that we have also accounted for the time taken to start the USRP and stop. 
#print('Sleeping for ', IntialSleep, ' seconds')
#time.sleep(IntialSleep)

while 1:
	countertoexit = 0

	while 1:
		if path.exists("/tmp/FileNameWritten.txt"):
			print('File received')
			f=open("/tmp/FileNameWritten.txt", "r")
			IQReceiveFileName = f.read()
			print("File Content", IQReceiveFileName)
			f.close()
			print(datetime.datetime.now().time())
			print('Deleting File: /tmp/FileNameWritten.txt', )
			os.system('sshpass -p \'123456\' sudo rm -rf /tmp/FileNameWritten.txt')
			print('File deleted')
			print(datetime.datetime.now().time())
			break
		else:
			time.sleep(waiteachiterationFilecheck) # Check every 100 ms if TX has sent file/ready to play.
			countertoexit = countertoexit + 1

			if int(countertoexit%30) == 0: # Every two seconds
				print('We are waiting to receive file')
			if countertoexit > (waitBeforeprogramexit/waiteachiterationFilecheck):
				print('We waited for ', waitBeforeprogramexit, ' seconds and since there is no indication of signal being played, we are exiting program ')
				print(datetime.datetime.now().time())
				sys.exit()

	print('We are sleeping for ', SleepAfterEachTest, ' seconds')
	print(datetime.datetime.now().time())
	time.sleep(SleepAfterEachTest)
	IQReceiveFileInfo = IQReceiveFileLocation + IQReceiveFileName
	commandLine = 'sshpass -v -p \'123456\' sudo python ' + pythonFile + ' ' + IQReceiveFileInfo + ' ' + str(DurationDataCollect)
	print('What we issue in command line is: ', commandLine)
	print('We are collecting data for', DurationDataCollect, ' seconds')
	print(datetime.datetime.now().time())
	os.system(commandLine)
	print('Data collection complete')
	print(datetime.datetime.now().time())

print('CollectComplete')












#for value in ModulationTypes:
#		now = datetime.now()
#		date_time = now.strftime("%m_%d_%Y_%H_%M")
#		
#		IQReceiveFileName = date_time + '_' + value + DataCollectAdditionalDetails
#		IQReceiveFileInfo = IQReceiveFileLocation + IQReceiveFileName
		# We have now created files with the appropriate mod type appended with the data and time
		
		# We now need to add correct values of time of collect and wait between each collect.
		# We collect as many time as there are modulation types.
		# We collect data for 40 seconds and sleep for 85 seconds after that.
		# We repeat this for all mod types. The sleep after last mod type is not necessary, doesn't hurt as well 
		
#		pythonFileLocation = '/home/venkatesh/Desktop/USRPProject/FlowGraphs/'
#		pythonFile = pythonFileLocation + 'ReceiveUsrpControl.py'
#		print('What we issue in command line is: ', commandLine)
#		print('We are collecting data for', )
#		os.system(commandLine)
#		print('Sleeping for ', SleepAfterEachTest, ' seconds')
#		time.sleep(SleepAfterEachTest)
#		print('Waking Up after sleep')	


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
