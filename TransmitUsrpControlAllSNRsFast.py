#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Playtonefromfile1
# GNU Radio version: 3.7.13.5
##################################################
#Thu 19 Sep 2019 11:47:05 AM PDT
from gnuradio import blocks
from gnuradio import eng_notation
from gnuradio import gr
from gnuradio import uhd
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from optparse import OptionParser
import pmt
import time
import sys
import os
import datetime


class PlayToneFromFIle1(gr.top_block):

    def __init__(self):
        gr.top_block.__init__(self, "Playtonefromfile1")

        ##################################################
        # Variables
        ##################################################
        self.samp_rate = samp_rate = 1250000
        self.carrier = carrier = 900000000
        self.TxGain = TxGain = 30
        self.RxGain = RxGain = 30
        ImaginaryFileName = sys.argv[2]
        RealFileName = sys.argv[1]
        print('Real File Name is ', RealFileName)
        print('Imaginary File Name is ', ImaginaryFileName)
        self.NumSeconds = NumSeconds = int(sys.argv[3])
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
        self.uhd_usrp_sink_0.set_time_now(uhd.time_spec(time.time()), uhd.ALL_MBOARDS)
        self.uhd_usrp_sink_0.set_center_freq(carrier, 0)
        self.uhd_usrp_sink_0.set_gain(TxGain, 0)
        self.uhd_usrp_sink_0.set_antenna('TX/RX', 0)
        self.uhd_usrp_sink_0.set_center_freq(carrier, 1)
        self.uhd_usrp_sink_0.set_gain(TxGain, 1)
        self.uhd_usrp_sink_0.set_antenna('TX/RX', 1)
        self.uhd_usrp_sink_0.set_center_freq(carrier, 2)
        self.uhd_usrp_sink_0.set_gain(TxGain, 2)
        self.uhd_usrp_sink_0.set_antenna('TX/RX', 2)
        self.uhd_usrp_sink_0.set_center_freq(carrier, 3)
        self.uhd_usrp_sink_0.set_gain(TxGain, 3)
        self.uhd_usrp_sink_0.set_antenna('TX/RX', 3)
        self.blocks_head_0 = blocks.head(gr.sizeof_gr_complex*1, NumSeconds*samp_rate)
        self.blocks_float_to_complex_0 = blocks.float_to_complex(1)
        self.blocks_file_source_0_0 = blocks.file_source(gr.sizeof_float*1, ImaginaryFileName, True)
        self.blocks_file_source_0_0.set_begin_tag(pmt.PMT_NIL)
        self.blocks_file_source_0 = blocks.file_source(gr.sizeof_float*1, RealFileName, True)
        self.blocks_file_source_0.set_begin_tag(pmt.PMT_NIL)
        self.blocks_null_source_0_1 = blocks.null_source(gr.sizeof_gr_complex*1)
        self.blocks_null_source_0_0 = blocks.null_source(gr.sizeof_gr_complex*1)
        self.blocks_null_source_0 = blocks.null_source(gr.sizeof_gr_complex*1)


        ##################################################
        # Connections
        ##################################################
        self.connect((self.blocks_file_source_0, 0), (self.blocks_float_to_complex_0, 0))
        self.connect((self.blocks_file_source_0_0, 0), (self.blocks_float_to_complex_0, 1))
        self.connect((self.blocks_float_to_complex_0, 0), (self.blocks_head_0, 0))
        self.connect((self.blocks_head_0, 0), (self.uhd_usrp_sink_0, 0))
        self.connect((self.blocks_null_source_0_1, 0), (self.uhd_usrp_sink_0, 1))
        self.connect((self.blocks_null_source_0_0, 0), (self.uhd_usrp_sink_0, 2))
        self.connect((self.blocks_null_source_0, 0), (self.uhd_usrp_sink_0, 3))

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

    def get_TxGain(self):
        return self.TxGain

    def set_TxGain(self, TxGain):
        self.TxGain = TxGain
        self.uhd_usrp_sink_0.set_gain(self.TxGain, 0)

        self.uhd_usrp_sink_0.set_gain(self.TxGain, 1)

        self.uhd_usrp_sink_0.set_gain(self.TxGain, 2)

        self.uhd_usrp_sink_0.set_gain(self.TxGain, 3)


    def get_RxGain(self):
        return self.RxGain
 
    def set_RxGain(self, RxGain):
        self.RxGain = RxGain

    def get_NumSeconds(self):
        return self.NumSeconds

    def set_NumSeconds(self, NumSeconds):
        self.NumSeconds = NumSeconds
        self.blocks_head_0.set_length(self.NumSeconds*self.samp_rate)



def main(top_block_cls=PlayToneFromFIle1, options=None):
    if gr.enable_realtime_scheduling() != gr.RT_OK:
        print("Error: failed to enable real-time scheduling.")

    tb = top_block_cls()
    tb.start()

# Test run from GeLu laptop
    #os.system('sshpass -p \'123456789\' /usr/bin/scp FileNameWritten.txt gelu@100.91.146.1:/tmp/')

# We are copying the file onto geLu laptop - the receive laptop. The receive laptop once it sees this file
# shall start its USRP and receive the signals. This mechanism is a crude way to co-ordinate transmit and receive prcess

####### COmmenitng this line only for small tests... This below line shud be uncommented. - Done July 12th.
    #os.system('sshpass -p \'123456789\' /usr/bin/scp FileNameWritten.txt gelu@100.91.146.1:/tmp/')
    os.system("cat FileNameWritten.txt")
    print('File sent')
    print(datetime.datetime.now().time())
    tb.wait()


if __name__ == '__main__':
    main()
