import sys
import glob
import os



label_dict = {0:'16QAM', 1:'64QAM', 2:'8PSK', 3:'BFM', 4:'BPSK', 5:'CPFSK', 6:'DSBAM', 7:'GFSK',
8:'PAM4', 9:'QPSK', 10:'SSBAM'}
print(len(sys.argv))
if len(sys.argv) == 1:
	filelocation = '/home/venkatesh/Desktop/USRPProject/DataCollect/IQSamples/Transmit/18thAugustCorrectScalingNoSNRSetNoChannelEffects/'
	filenameReal =  glob.glob(filelocation + 'QPSK' + '*' + 'Real.bin')
	filenameImag =  glob.glob(filelocation + 'QPSK' + '*' + 'Imag.bin')
elif len(sys.argv) ==2:
	filelocation = '/home/venkatesh/Desktop/USRPProject/DataCollect/IQSamples/Transmit/18thAugustCorrectScalingNoSNRSetNoChannelEffects/'	
	filenameReal =  glob.glob(filelocation + sys.argv[1] + '*' + 'Real.bin')
	filenameImag =  glob.glob(filelocation + sys.argv[1] + '*' + 'Imag.bin')
else:
	filelocation = sys.argv[2]
	filenameReal =  glob.glob(filelocation + sys.argv[1] + '*' + 'Real.bin')
	filenameImag =  glob.glob(filelocation + sys.argv[1] + '*' + 'Imag.bin')

filenameReal = str(filenameReal[0])
filenameImag = str(filenameImag[0])
	
print('File played: ', filenameReal, ' \n ', filenameImag, '\n')
print('File Location: ', filelocation)



sudo apt update
sudo apt install openssh-server
sudo s  ystemctl status ssh



/Users/venkat/Documents/ModulationClassificationOTA/IQSamples/

		
