#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Receivedataautomated
# GNU Radio version: 3.7.13.5
##################################################

from gnuradio import blocks
from gnuradio import eng_notation
from gnuradio import gr
from gnuradio import uhd
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from optparse import OptionParser
import time
import sys


class ReceiveDataAutomated(gr.top_block):

    def __init__(self):
        gr.top_block.__init__(self, "Receivedataautomated")

        ##################################################
        # Variables
        ##################################################
        self.samp_rate = samp_rate = 125000000/100
        self.carrier = carrier = 1500000000
	Chain1FileName = sys.argv[1]+'_chain1.bin'
	Chain2FileName = sys.argv[1]+'_chain2.bin'	
	Chain3FileName = sys.argv[1]+'_chain3.bin'
	Chain4FileName = sys.argv[1]+'_chain4.bin'
        self.RXGainSlider = RXGainSlider = 18
        self.NumSeconds = NumSeconds = int(sys.argv[2])

        ##################################################
        # Blocks
        ##################################################
        self.uhd_usrp_source_0 = uhd.usrp_source(
        	",".join(("addr=192.168.10.2", "")),
        	uhd.stream_args(
        		cpu_format="fc32",
        		channels=range(4),
        	),
        )
        self.uhd_usrp_source_0.set_samp_rate(samp_rate)
        self.uhd_usrp_source_0.set_center_freq(carrier, 0)
        self.uhd_usrp_source_0.set_gain(RXGainSlider, 0)
        self.uhd_usrp_source_0.set_antenna('RX2', 0)
        self.uhd_usrp_source_0.set_auto_dc_offset(True, 0)
        self.uhd_usrp_source_0.set_auto_iq_balance(True, 0)
        self.uhd_usrp_source_0.set_center_freq(carrier, 1)
        self.uhd_usrp_source_0.set_gain(RXGainSlider, 1)
        self.uhd_usrp_source_0.set_antenna('RX2', 1)
        self.uhd_usrp_source_0.set_auto_dc_offset(True, 1)
        self.uhd_usrp_source_0.set_auto_iq_balance(True, 1)
        self.uhd_usrp_source_0.set_center_freq(carrier, 2)
        self.uhd_usrp_source_0.set_gain(RXGainSlider, 2)
        self.uhd_usrp_source_0.set_antenna('RX2', 2)
        self.uhd_usrp_source_0.set_auto_dc_offset(True, 2)
        self.uhd_usrp_source_0.set_auto_iq_balance(True, 2)
        self.uhd_usrp_source_0.set_center_freq(carrier, 3)
        self.uhd_usrp_source_0.set_gain(RXGainSlider, 3)
        self.uhd_usrp_source_0.set_antenna('RX2', 3)
        self.uhd_usrp_source_0.set_auto_dc_offset(True, 3)
        self.uhd_usrp_source_0.set_auto_iq_balance(True, 3)
        self.blocks_head_0_2 = blocks.head(gr.sizeof_gr_complex*1, NumSeconds*samp_rate)
        self.blocks_head_0_1 = blocks.head(gr.sizeof_gr_complex*1, NumSeconds*samp_rate)
        self.blocks_head_0_0 = blocks.head(gr.sizeof_gr_complex*1, NumSeconds*samp_rate)
        self.blocks_head_0 = blocks.head(gr.sizeof_gr_complex*1, NumSeconds*samp_rate)
        self.blocks_file_sink_0_0_0_0 = blocks.file_sink(gr.sizeof_gr_complex*1, Chain1FileName, False)
        self.blocks_file_sink_0_0_0_0.set_unbuffered(False)
        self.blocks_file_sink_0_0_0 = blocks.file_sink(gr.sizeof_gr_complex*1, Chain2FileName, False)
        self.blocks_file_sink_0_0_0.set_unbuffered(False)
        self.blocks_file_sink_0_0 = blocks.file_sink(gr.sizeof_gr_complex*1, Chain3FileName, False)
        self.blocks_file_sink_0_0.set_unbuffered(False)
        self.blocks_file_sink_0 = blocks.file_sink(gr.sizeof_gr_complex*1, Chain4FileName, False)
        self.blocks_file_sink_0.set_unbuffered(False)



        ##################################################
        # Connections
        ##################################################
        self.connect((self.blocks_head_0, 0), (self.blocks_file_sink_0_0_0_0, 0))
        self.connect((self.blocks_head_0_0, 0), (self.blocks_file_sink_0_0_0, 0))
        self.connect((self.blocks_head_0_1, 0), (self.blocks_file_sink_0, 0))
        self.connect((self.blocks_head_0_2, 0), (self.blocks_file_sink_0_0, 0))
        self.connect((self.uhd_usrp_source_0, 0), (self.blocks_head_0, 0))
        self.connect((self.uhd_usrp_source_0, 1), (self.blocks_head_0_0, 0))
        self.connect((self.uhd_usrp_source_0, 2), (self.blocks_head_0_1, 0))
        self.connect((self.uhd_usrp_source_0, 3), (self.blocks_head_0_2, 0))

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.uhd_usrp_source_0.set_samp_rate(self.samp_rate)
        self.blocks_head_0_2.set_length(self.NumSeconds*self.samp_rate)
        self.blocks_head_0_1.set_length(self.NumSeconds*self.samp_rate)
        self.blocks_head_0_0.set_length(self.NumSeconds*self.samp_rate)
        self.blocks_head_0.set_length(self.NumSeconds*self.samp_rate)

    def get_carrier(self):
        return self.carrier

    def set_carrier(self, carrier):
        self.carrier = carrier
        self.uhd_usrp_source_0.set_center_freq(self.carrier, 0)
        self.uhd_usrp_source_0.set_center_freq(self.carrier, 1)
        self.uhd_usrp_source_0.set_center_freq(self.carrier, 2)
        self.uhd_usrp_source_0.set_center_freq(self.carrier, 3)

    def get_RXGainSlider(self):
        return self.RXGainSlider

    def set_RXGainSlider(self, RXGainSlider):
        self.RXGainSlider = RXGainSlider
        self.uhd_usrp_source_0.set_gain(self.RXGainSlider, 0)

        self.uhd_usrp_source_0.set_gain(self.RXGainSlider, 1)

        self.uhd_usrp_source_0.set_gain(self.RXGainSlider, 2)

        self.uhd_usrp_source_0.set_gain(self.RXGainSlider, 3)


    def get_NumSeconds(self):
        return self.NumSeconds

    def set_NumSeconds(self, NumSeconds):
        self.NumSeconds = NumSeconds
        self.blocks_head_0_2.set_length(self.NumSeconds*self.samp_rate)
        self.blocks_head_0_1.set_length(self.NumSeconds*self.samp_rate)
        self.blocks_head_0_0.set_length(self.NumSeconds*self.samp_rate)
        self.blocks_head_0.set_length(self.NumSeconds*self.samp_rate)


def main(top_block_cls=ReceiveDataAutomated, options=None):
    if gr.enable_realtime_scheduling() != gr.RT_OK:
        print "Error: failed to enable real-time scheduling."

    tb = top_block_cls()
    tb.start()
    tb.wait()


if __name__ == '__main__':
    main()
