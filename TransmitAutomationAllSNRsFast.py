import os
import string
import time
import datetime
############################################################
################ STATE DIAGRAM  ############################
############################################################
# Send dummy file with signal type info written to it - to receiver laptop(indirect way of synchronizing the TX and RX controlling laptops and also pasisng on 
#info about the type of signal being transmitted), play file for 100 seconds and then wait for 10 seconds.

ModulationTypes = ["BPSK", "QPSK", "8PSK", \
  "16QAM", "64QAM", "PAM4", "GFSK", "CPFSK", \
  "BFM", "DSBAM", "SSBAM"]

#TransmitFileLocation = '/home/venkatesh/Desktop/USRPProject/DataCollect/IQSamples/Transmit/13SepDataForPaper/'
# files moved to Documents on July 10th. Therefore chaningg the folder location accordingly.
TransmitFileLocation = '/home/venkatesh/Documents/USRPProject/DataCollect/IQSamples/Transmit/13SepDataForPaper/'
#transmitFilePartialReal = '18thAug2019EvenReal.bin'
#transmitFilePartialImag = '18thAug2019EvenImag.bin'

# files moved to Documents on July 10th. Therefore chaningg the folder location accordingly.
pythonUSRPcontrolFileLocation = '/home/venkatesh/Documents/USRPProject/FlowGraphs/' 
pythonUSRPcontrolFileName = pythonUSRPcontrolFileLocation + 'TransmitUsrpControlAllSNRsFast.py'
DataTransmitDuration = 25
#DataTransmitDuration = 10
SleepDuration = 5

print('Deleting FileNameWritten.txt in /tmp folder of receive laptop before test start.')
os.system('/home/venkatesh/Documents/USRPProject/FlowGraphs/deleteFileBeforeTest.sh')
initialSleep = 10 # We are giving sufficient time for us to start the reception automation after we start this transmission automation.


#print(' We are giving sufficient time for us to start the reception automation after we start this transmission automation.')
#print('Sleeping for ', initialSleep, ' seconds')
#time.sleep(initialSleep)
#print(datetime.datetime.now().time())

print('We are running USRP speed test - benchmar tests. We have noticed frequent L errors and these tests help avoid them.')
os.system('sshpass -p \'123456\' /home/venkatesh/Documents/USRPProject/FlowGraphs/usrptest.sh')
for SNR in range(20,-21,-2):
    
    #print('We are running USRP speed test - benchmar tests. We have noticed frequent L errors and these tests help avoid them.')
    #os.system('sshpass -p \'123456\' /home/venkatesh/Desktop/USRPProject/FlowGraphs/usrptest.sh')
    
    if SNR < 0:
        SNRString = 'minus' + str(SNR*-1)
    else:
        SNRString = str(SNR)
    for modulationvalue in ModulationTypes:
        
        #filenametoreceiver = 'SNR' + SNRString + '_' + modulationvalue + '_Receive.bin'
        #handle=open('FileNameWritten.txt','w+')
        #handle.write(filenametoreceiver)
        #handle.close();
        #os.system('sshpass -p \'123456789\' /usr/bin/scp FileNameWritten.txt gelu@100.91.146.1:/tmp/')
        filenametoreceiver = 'SNR' + SNRString + '_' + modulationvalue + '_Receive.bin'
        handle=open('FileNameWritten.txt','w+')	
        handle.write(filenametoreceiver)
        handle.close();
        #print('File sent')
        #print(datetime.datetime.now().time())
        #os.system('sshpass -P ')
        transmitFileReal = TransmitFileLocation + 'SNR' + SNRString + '_' + modulationvalue + 'Real.bin'
        transmitFileImag = TransmitFileLocation + 'SNR' + SNRString + '_' + modulationvalue + 'Imag.bin'
        #commandlineVal = 'sshpass -v -p \'123456789\' sudo python ' + pythonUSRPcontrolFileName + ' ' + transmitFileReal + ' ' + transmitFileImag + ' ' + str(DataTransmitDuration)
        commandlineVal = 'python2 ' + pythonUSRPcontrolFileName + ' ' + transmitFileReal + ' ' + transmitFileImag + ' ' + str(DataTransmitDuration)
        print('Commandline issued is: ', commandlineVal)
        print(datetime.datetime.now().time())
        os.system(commandlineVal)
        print('Transmit Complete')
        print(datetime.datetime.now().time())
        print('Sleeping ', SleepDuration, ' seconds')
        time.sleep(SleepDuration)
        print('Waking Up to send file across')
        print(datetime.datetime.now().time())

























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
