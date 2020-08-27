#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 25 20:15:20 2020

@author: venkatesh
"""

## Refer to https://www.gnuradio.org/doc/doxygen/ for GNURadio documentation

import os
#import string
import time
import datetime
from os import path
from TransmitUSRPControl_SetSNRviaHW import TransmitModulationData
from SetProgrammableAttenuator import set_programamble_attenuator_function
import numpy as np
from LoggerPython import Logger
import sys
############################################################
################ STATE DIAGRAM  ############################
############################################################
# Send dummy file with signal type info written to it - to receiver laptop(indirect way of synchronizing the TX and RX controlling laptops and also pasisng on 
#info about the type of signal being transmitted), play file for DataTransmitDuration seconds and then wait for SleepDuration seconds-repeat for all modulations.

ModulationTypes = ["BPSK", "QPSK", "8PSK", \
  "16QAM", "64QAM", "PAM4", "GFSK", "CPFSK", \
  "BFM", "DSBAM", "SSBAM"]

SNRStep = 2
TransmitFileLocation = '/home/venkatesh/Documents/USRPProject/DataCollect/IQSamples/Transmit/12August2020_TransmitNoAWGN/'
RX_IPAddress =  '100.89.81.145'#'137.110.40.157'#'100.108.67.213'#'100.64.70.42'#'100.89.81.145'#'100.64.89.119'
samp_rate = 1250000 
carrier = 990000000
TxGain = 30

# We are logging the infrmation onto a log file
now = datetime.datetime.now()
date_time = now.strftime("%m_%d_%Y_%H_%M_%S")
logfilelocation = '/home/venkatesh/Documents/USRPProject/FlowGraphs/USRPControlFiles/logs/'
logfilename = logfilelocation + '_' + date_time + '.txt'
sys.stdout = Logger(logfilename)


pythonUSRPcontrolFileLocation = '/home/venkatesh/Documents/USRPProject/FlowGraphs/USRPControlFiles/' 
pythonUSRPcontrolFileName = pythonUSRPcontrolFileLocation + 'TransmitUsrpControlAllSNRsFast.py'
DataTransmitDuration = 1
SleepDuration = 0.5

print('Deleting ModulationAndSNR.txt and computed_power.txt in /tmp folder of receive laptop before test start.')
#os.system('/home/venkatesh/Documents/USRPProject/FlowGraphs/deleteFileBeforeTest.sh')
#os.system('sshpass -p \'123456\' sudo rm -rf /tmp/ModulationAndSNR.txt')
#os.system('sshpass -p \'123456\' sudo rm -rf /tmp/computed_power.txt')

#print('We are running USRP speed test - benchmark tests. We have noticed frequent L errors and these tests help avoid them.')
#os.system('cat ' + pythonUSRPcontrolFileLocation + 'usrptest.sh ')
#os.system('sshpass -p \'123456\' ' + pythonUSRPcontrolFileLocation + 'usrptest.sh')
#
#time.sleep(10)
#print('We are sleeping for 10 seconds to give the user time to start RX automation')
## We are now calculating noise power after transmitting a signal.

handle=open('compute_power.txt','w+')    
handle.write('Computing Noise power')
handle.close()
print('We are now calculating noise power after transmitting a signal. File being sent to RX')
os.system('sshpass -p \'123456789\' /usr/bin/scp compute_power.txt gelu@' + RX_IPAddress + ':/tmp/')

while 1:
    if path.exists("/tmp/computed_power.txt"):
        print('Received Noise power file')
        time.sleep(0.5)# Waiting for half a second so that file is properly saved onto the tmp folder of RX host
        f=open("/tmp/computed_power.txt", "r")
        computednoisepower = f.read()
        print(computednoisepower)
        computednoisepower = float(computednoisepower)
        print("Computed noise power", computednoisepower)
        f.close()
        time.sleep(0.3)
#        os.system('sshpass -p \'123456\' sudo rm -rf /tmp/computed_power.txt')
        time.sleep(0.3)
        break    
    

for modulationvalue in ModulationTypes:

    # Set value of progammable attenuator
    atten_R30_1 = 0
    atten_R40_1 = 15 
    set_both_attenuators = 1
    set_programamble_attenuator_function(atten_R30_1, atten_R40_1)

    # We are now calculating signal power after transmitting a signal.
    
    print("Sending compute_file to RX")
    os.system('sshpass -p \'123456789\' /usr/bin/scp compute_power.txt gelu@'+RX_IPAddress+':/tmp/')
    
    print("Transmitting Signal for signal power computation by RX for ",DataTransmitDuration,' seconds.')
    real_filename_fortransmit = TransmitFileLocation + modulationvalue + 'Transmitdata_NoAWGNReal.bin'
    imag_filename_fortransmit = TransmitFileLocation + modulationvalue + 'Transmitdata_NoAWGNImag.bin'
    print(datetime.datetime.now().time())
    #samp_rate, carrier, TxGain, RealFileName, ImaginaryFileName,NumSeconds
    tb = TransmitModulationData(samp_rate, carrier, TxGain, real_filename_fortransmit, imag_filename_fortransmit,DataTransmitDuration)
    print("TX USRP starting up for transmitting signal for power computation")
    tb.start()
    tb.wait()
    del tb
    print('Transmit Complete')
    print('Sleeping for 2 seconds after tranmit complete')
    time.sleep(2)

    while 1:
        print('Hi')
        if path.exists("/tmp/computed_power.txt"):
            print('Received Signal power file')
            time.sleep(0.5)# Waiting for half a second so that file is properly saved onto the tmp folder of RX host
            f=open("/tmp/computed_power.txt", "r")
            computedsignalpower = f.read()
            print(computedsignalpower)
            computedsignalpower = float(computedsignalpower)
            print("Computed signal power", computedsignalpower)
            f.close()
            time.sleep(0.3)
#            os.system('sshpass -p \'123456\' sudo rm -rf /tmp/computed_power.txt')
            time.sleep(0.3)
            break    
            
    # We are calculating what attenuation to set for 20dB based on our measured signa power
    atten_change =  computedsignalpower - computednoisepower - 20
    # We need to round the attenuation to be set closest to 0.25 since the resolution of the programmable atten is 0.25
    programm_atten_resolution = 0.25
    atten_change = (np.round(atten_change/programm_atten_resolution))*programm_atten_resolution
    print("Attempting to change attenuation to set 20dB",atten_change)
    
    # If the attenuation to be set is in between -15 and + +15, we only change the R_30 attenuator and not touch R_40 
    # This is because the prgrammable attenuators have a range of 0 to 30. 
    #R_30 and R40 are the two attenuators with the IP addresses 192.168.30.1 and 192.168.40.1
    # If the attenuation to be set is more than this range, set the R40 with the residual of r30_atten +/- 15. 
#    if atten_change <= 15 and atten_change >= -15:
#        atten_R30_1 = atten_R30_1 + atten_change
#        set_both_attenuators = 0
#        set_programamble_attenuator_function(atten_R30_1,set_both_attenuators)
#
#    else:
#        if atten_change > 15:
#            atten_change_30_1 = 15
#            atten_change_40_1 = atten_change - atten_change_30_1
#        else:
#            atten_change_30_1 = -15
#            atten_change_40_1 = atten_change - atten_change_30_1
#        
#        atten_R30_1 = atten_R30_1 + atten_change_30_1
#        atten_R40_1 = atten_R40_1 + atten_change_40_1
#        set_both_attenuators = 1
#        set_programamble_attenuator_function([atten_R30_1, atten_R40_1],set_both_attenuators)

    if (atten_change + atten_R40_1 <= 30) and (atten_change + atten_R40_1 >= 0):
        atten_R40_1 = atten_R40_1 + atten_change
        
    elif atten_change + atten_R40_1 > 30:
        atten_R30_1 = (atten_change + atten_R40_1 - 30) + atten_R30_1
        atten_R40_1 = 30
    elif atten_change + atten_R40_1 < 0:
        atten_R30_1 = (atten_change + atten_R40_1) + atten_R30_1
        atten_R40_1 = 0
        
    set_programamble_attenuator_function(atten_R30_1, atten_R40_1)

    # Compute signal power after setting attenuation to achieve 20dB as a sanity cehck
    print("Compute signal power after setting attenuation to achieve 20dB as a sanity check")
    
    print("Sending compute_file to RX")
    os.system('sshpass -p \'123456789\' /usr/bin/scp compute_power.txt gelu@'+RX_IPAddress+':/tmp/')
#        os.system('sshpass -p \'123456789\' /usr/bin/scp compute_power.txt gelu@'+RX_IPAddress+':/tmp/')
    print("Transmitting Signal for signal power computation by RX for ",DataTransmitDuration,' seconds.for sanity test')
    real_filename_fortransmit = TransmitFileLocation + modulationvalue + 'Transmitdata_NoAWGNReal.bin'
    imag_filename_fortransmit = TransmitFileLocation + modulationvalue + 'Transmitdata_NoAWGNImag.bin'
    print(datetime.datetime.now().time())
    #samp_rate, carrier, TxGain, RealFileName, ImaginaryFileName,NumSeconds
    tb = TransmitModulationData(samp_rate, carrier, TxGain, real_filename_fortransmit, imag_filename_fortransmit,DataTransmitDuration)
    print("TX USRP starting up for transmitting signal for power computation")
    tb.start()
    tb.wait()
    del tb
    print('Transmit Complete')
    print('Sleeping for 2 seconds after tranmit complete')
    time.sleep(2)
    
    while 1:
        if path.exists("/tmp/computed_power.txt"):
            print('Received Signal power file')
            time.sleep(0.5)# Waiting for half a second so that file is properly saved onto the tmp folder of RX host
            f=open("/tmp/computed_power.txt", "r")
            computedsignalpower = f.read()
            print(computedsignalpower)
            computedsignalpower = float(computedsignalpower)
            print("Computed signal power", computedsignalpower)
            f.close()
            time.sleep(0.3)
#            os.system('sshpass -p \'123456\' sudo rm -rf /tmp/computed_power.txt')
            time.sleep(0.3)
            break
    print("Signal power minus noise power now is: ", computedsignalpower - computednoisepower)
    print("Ensure that this difference is not too off from intended 20dB")
    


    for SNR in range(20,-21,-1*SNRStep):
        
        #print('We are running USRP speed test - benchmar tests. We have noticed frequent L errors and these tests help avoid them.')
        #os.system('sshpass -p \'123456\' /home/venkatesh/Desktop/USRPProject/FlowGraphs/usrptest.sh')
        if SNR < 0:
            SNRString = 'minus' + str(SNR*-1)
        else:
            SNRString = str(SNR)
            
        # Transfer the file contaning the modulation and SNR of the data transmitted
        print("Modulation and SNR that we are about to transmit are: ", modulationvalue, SNR)
        
        print("Setting external attenuators to set teh requisite power")
        if SNR != 20:
            atten_change = SNRStep
            #atten_change = (np.round(atten_change/programm_atten_resolution))*programm_atten_resolution
            if (atten_change + atten_R40_1 <= 30) and (atten_change + atten_R40_1 >= 0):
                atten_R40_1 = atten_R40_1 + atten_change
            
            elif atten_change + atten_R40_1 > 30:
                atten_R30_1 = (atten_change + atten_R40_1 - 30) + atten_R30_1
                atten_R40_1 = 30
            elif atten_change + atten_R40_1 < 0:
                atten_R30_1 = (atten_change + atten_R40_1) + atten_R30_1
                atten_R40_1 = 0
            set_programamble_attenuator_function(atten_R30_1, atten_R40_1)
                    
        
        mod_and_snr = modulationvalue + '_' + 'SNR' + SNRString + '_Receive.bin'
        handle=open('ModulationAndSNR.txt','w+')    
        handle.write(mod_and_snr)
        handle.close()
        print("We are now transferring a file with the modulation and SNR of the data to indicate RX system to start capture")
        os.system('sshpass -p \'123456789\' /usr/bin/scp ModulationAndSNR.txt gelu@'+RX_IPAddress+':/tmp/')
        os.system("cat ModulationAndSNR.txt")
        #print('File sent')
        
        real_filename_fortransmit = TransmitFileLocation + modulationvalue + 'Transmitdata_NoAWGNReal.bin'
        imag_filename_fortransmit = TransmitFileLocation + modulationvalue + 'Transmitdata_NoAWGNImag.bin'
        print(datetime.datetime.now().time())
        #samp_rate, carrier, TxGain, RealFileName, ImaginaryFileName,NumSeconds
        tb = TransmitModulationData(samp_rate, carrier, TxGain, real_filename_fortransmit, imag_filename_fortransmit,DataTransmitDuration)
        print("TX USRP starting up")
        #tb.start()
        #tb.wait()
        tb.run()
        del tb
        #tb.stop()
        print('Transmit Complete')
        print(datetime.datetime.now().time())
        print('Sleeping ', SleepDuration, ' seconds')
        time.sleep(SleepDuration)
        print('Waking UP')
        print(datetime.datetime.now().time())

# Test run from GeLu laptop
    #os.system('sshpass -p \'123456789\' /usr/bin/scp FileNameWritten.txt gelu@100.91.146.1:/tmp/')

# We are copying the file onto geLu laptop - the receive laptop. The receive laptop once it sees this file
# shall start its USRP and receive the signals. This mechanism is a crude way to co-ordinate transmit and receive prcess

####### COmmenitng this line only for small tests... This below line shud be uncommented. - Done July 12th.

    
    
    
        #for modulationvalue in ModulationTypes:
            
            #filenametoreceiver = 'SNR' + SNRString + '_' + modulationvalue + '_Receive.bin'
            #handle=open('ModulationAndSNR.txt','w+')
            #handle.write(filenametoreceiver)
            #handle.close();
#            
#            filenametoreceiver = 'SNR' + SNRString + '_' + modulationvalue + '_Receive.bin'
#            handle=open('ModulationAndSNR.txt','w+')    
#            handle.write(filenametoreceiver)
#            os.system('sshpass -p \'123456789\' /usr/bin/scp ModulationAndSNR.txt gelu@'+RX_IPAddress+':/tmp/')
#            handle.close();
            #print('File sent')
            #print(datetime.datetime.now().time())
            #os.system('sshpass -P ')
#            transmitFileReal = TransmitFileLocation + 'SNR' + SNRString + '_' + modulationvalue + 'Real.bin'
#            transmitFileImag = TransmitFileLocation + 'SNR' + SNRString + '_' + modulationvalue + 'Imag.bin'
#            #commandlineVal = 'sshpass -v -p \'123456789\' sudo python ' + pythonUSRPcontrolFileName + ' ' + transmitFileReal + ' ' + transmitFileImag + ' ' + str(DataTransmitDuration)
#            commandlineVal = 'python2 ' + pythonUSRPcontrolFileName + ' ' + transmitFileReal + ' ' + transmitFileImag + ' ' \
#            + str(DataTransmitDuration)
#            print('Commandline issued is: ', commandlineVal)
#            print(datetime.datetime.now().time())
#            os.system(commandlineVal)





