#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Playfile
# GNU Radio version: 3.7.13.5
##################################################

from gnuradio import blocks
from gnuradio import eng_notation
from gnuradio import gr
from gnuradio import uhd
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from optparse import OptionParser
import pmt
import time
import glob
import sys
import os

class PlayFile(gr.top_block):

    def __init__(self):
        gr.top_block.__init__(self, "Playfile")
	#os.system('./usrptest_short.sh')
	#time.sleep(4)

        ##################################################
        # Variables
        ##################################################
        self.samp_rate = samp_rate = 250e3
        self.carrier = carrier = 900000000
	self.NumSeconds = NumSeconds = int(20)
        ##################################################
        # Blocks
        ##################################################
        self.uhd_usrp_sink_0 = uhd.usrp_sink(
        	",".join(("addr=192.168.10.2", "")),
        	uhd.stream_args(
        		cpu_format="fc32",
        		channels=range(4),
        	),
        )
        self.uhd_usrp_sink_0.set_samp_rate(samp_rate)
        self.uhd_usrp_sink_0.set_center_freq(carrier, 0)
        self.uhd_usrp_sink_0.set_gain(20, 0)
        self.uhd_usrp_sink_0.set_antenna('TX/RX', 0)
        self.uhd_usrp_sink_0.set_center_freq(carrier, 1)
        self.uhd_usrp_sink_0.set_gain(20, 1)
        self.uhd_usrp_sink_0.set_antenna('TX/RX', 1)
        self.uhd_usrp_sink_0.set_center_freq(carrier, 2)
        self.uhd_usrp_sink_0.set_gain(0, 2)
        self.uhd_usrp_sink_0.set_antenna('TX/RX', 2)
        self.uhd_usrp_sink_0.set_center_freq(carrier, 3)
        self.uhd_usrp_sink_0.set_gain(0, 3)
        self.uhd_usrp_sink_0.set_antenna('TX/RX', 3)
        self.blocks_null_source_0_1 = blocks.null_source(gr.sizeof_gr_complex*1)
        self.blocks_null_source_0_0 = blocks.null_source(gr.sizeof_gr_complex*1)
        self.blocks_null_source_0 = blocks.null_source(gr.sizeof_gr_complex*1)
        self.blocks_float_to_complex_0 = blocks.float_to_complex(1)
	self.blocks_head_0 = blocks.head(gr.sizeof_gr_complex*1, NumSeconds*samp_rate)
	label_dict = {0:'16QAM', 1:'64QAM', 2:'8PSK', 3:'BFM', 4:'BPSK', 5:'CPFSK', 6:'DSBAM', 7:'GFSK',
 	8:'PAM4', 9:'QPSK', 10:'SSBAM'}
	if len(sys.argv) == 1:
		filelocation = '/home/venkatesh/Desktop/USRPProject/DataCollect/IQSamples/Transmit/18thAugustCorrectScalingNoSNRSetNoChannelEffects/'
		filenameReal =  glob.glob(filelocation + 'QPSK' + '*' + 'Real.bin')
		filenameImag =  glob.glob(filelocation + 'QPSK' + '*' + 'Imag.bin')
	elif len(sys.argv) ==2:
		filelocation = sys.argv[1]
		filenameReal =  glob.glob(filelocation + 'QPSK' + '*' + 'Real.bin')
		filenameImag =  glob.glob(filelocation + 'QPSK' + '*' + 'Imag.bin')
		#filelocation = '/home/venkatesh/Desktop/USRPProject/DataCollect/IQSamples/Transmit/18thAugustCorrectScalingNoSNRSetNoChannelEffects/'	
		#filenameReal =  glob.glob(filelocation + sys.argv[1] + '*' + 'Real.bin')
		#filenameImag =  glob.glob(filelocation + sys.argv[1] + '*' + 'Imag.bin')
	else:
		filelocation = sys.argv[1]
		filenameReal =  glob.glob(filelocation + sys.argv[2] + '*' + 'Real.bin')
		filenameImag =  glob.glob(filelocation + sys.argv[2] + '*' + 'Imag.bin')
                print(filelocation)
                print(filenameReal)

	filenameReal = str(filenameReal[0])
	filenameImag = str(filenameImag[0])
	
	print('File played: ', filenameReal, ' \n ', filenameImag, '\n')
	print('File Location: ', filelocation)
        self.blocks_file_source_0_0 = blocks.file_source(gr.sizeof_float*1, filenameReal, True)
        self.blocks_file_source_0_0.set_begin_tag(pmt.PMT_NIL)
        self.blocks_file_source_0 = blocks.file_source(gr.sizeof_float*1, filenameImag, True)
        self.blocks_file_source_0.set_begin_tag(pmt.PMT_NIL)



        ##################################################
        # Connections
        ##################################################
        self.connect((self.blocks_file_source_0, 0), (self.blocks_float_to_complex_0, 1))
        self.connect((self.blocks_file_source_0_0, 0), (self.blocks_float_to_complex_0, 0))
        #self.connect((self.blocks_float_to_complex_0, 0), (self.uhd_usrp_sink_0, 0))
        self.connect((self.blocks_null_source_0, 0), (self.uhd_usrp_sink_0, 2))
        self.connect((self.blocks_null_source_0_0, 0), (self.uhd_usrp_sink_0, 3))
        self.connect((self.blocks_null_source_0_1, 0), (self.uhd_usrp_sink_0, 1))
	self.connect((self.blocks_float_to_complex_0, 0), (self.blocks_head_0, 0))
        self.connect((self.blocks_head_0, 0), (self.uhd_usrp_sink_0, 0))

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.uhd_usrp_sink_0.set_samp_rate(self.samp_rate)
	self.blocks_head_0.set_length(self.NumSeconds*self.samp_rate)
    def get_carrier(self):
        return self.carrier

    def set_carrier(self, carrier):
        self.carrier = carrier
        self.uhd_usrp_sink_0.set_center_freq(self.carrier, 0)
        self.uhd_usrp_sink_0.set_center_freq(self.carrier, 1)
        self.uhd_usrp_sink_0.set_center_freq(self.carrier, 2)
        self.uhd_usrp_sink_0.set_center_freq(self.carrier, 3)

    def set_NumSeconds(self, NumSeconds):
        self.NumSeconds = NumSeconds
        self.blocks_head_0.set_length(self.NumSeconds*self.samp_rate)


def main(top_block_cls=PlayFile, options=None):
    if gr.enable_realtime_scheduling() != gr.RT_OK:
        print("Error: failed to enable real-time scheduling.")
    tb = top_block_cls()
    time.sleep(1)
    tb.start()
    #try:
     #   raw_input('Press Enter to quit: ')
    #except EOFError:
    #    pass
    #tb.stop()
    tb.wait()


if __name__ == '__main__':
    main()
