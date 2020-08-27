#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Tutorial Two 1
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


class tutorial_two_1(gr.top_block):

    def __init__(self):
        gr.top_block.__init__(self, "Tutorial Two 1")

        ##################################################
        # Variables
        ##################################################
        self.txgainslider = txgainslider = 30
        self.samp_rate = samp_rate = 1.25e6
        self.carrier = carrier = 990e6

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
        self.uhd_usrp_sink_0.set_gain(txgainslider, 0)
        self.uhd_usrp_sink_0.set_antenna('TX/RX', 0)
        self.uhd_usrp_sink_0.set_center_freq(carrier, 1)
        self.uhd_usrp_sink_0.set_gain(txgainslider, 1)
        self.uhd_usrp_sink_0.set_antenna('TX/RX', 1)
        self.uhd_usrp_sink_0.set_center_freq(carrier, 2)
        self.uhd_usrp_sink_0.set_gain(txgainslider, 2)
        self.uhd_usrp_sink_0.set_antenna('TX/RX', 2)
        self.uhd_usrp_sink_0.set_center_freq(carrier, 3)
        self.uhd_usrp_sink_0.set_gain(txgainslider, 3)
        self.uhd_usrp_sink_0.set_antenna('TX/RX', 3)
        self.blocks_null_source_0_2 = blocks.null_source(gr.sizeof_gr_complex*1)
        self.blocks_null_source_0_1 = blocks.null_source(gr.sizeof_gr_complex*1)
        self.blocks_null_source_0 = blocks.null_source(gr.sizeof_gr_complex*1)
        self.blocks_float_to_complex_0 = blocks.float_to_complex(1)
        self.blocks_file_source_0_0 = blocks.file_source(gr.sizeof_float*1, '/home/venkatesh/Documents/USRPProject/DataCollect/IQSamples/Transmit/12August2020_TransmitNoAWGN/BPSKTransmitdata_NoAWGNImag.bin', True)
        self.blocks_file_source_0_0.set_begin_tag(pmt.PMT_NIL)
        self.blocks_file_source_0 = blocks.file_source(gr.sizeof_float*1, '/home/venkatesh/Documents/USRPProject/DataCollect/IQSamples/Transmit/12August2020_TransmitNoAWGN/BPSKTransmitdata_NoAWGNReal.bin', True)
        self.blocks_file_source_0.set_begin_tag(pmt.PMT_NIL)



        ##################################################
        # Connections
        ##################################################
        self.connect((self.blocks_file_source_0, 0), (self.blocks_float_to_complex_0, 0))
        self.connect((self.blocks_file_source_0_0, 0), (self.blocks_float_to_complex_0, 1))
        self.connect((self.blocks_float_to_complex_0, 0), (self.uhd_usrp_sink_0, 0))
        self.connect((self.blocks_null_source_0, 0), (self.uhd_usrp_sink_0, 1))
        self.connect((self.blocks_null_source_0_1, 0), (self.uhd_usrp_sink_0, 3))
        self.connect((self.blocks_null_source_0_2, 0), (self.uhd_usrp_sink_0, 2))

    def get_txgainslider(self):
        return self.txgainslider

    def set_txgainslider(self, txgainslider):
        self.txgainslider = txgainslider
        self.uhd_usrp_sink_0.set_gain(self.txgainslider, 0)

        self.uhd_usrp_sink_0.set_gain(self.txgainslider, 1)

        self.uhd_usrp_sink_0.set_gain(self.txgainslider, 2)

        self.uhd_usrp_sink_0.set_gain(self.txgainslider, 3)


    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.uhd_usrp_sink_0.set_samp_rate(self.samp_rate)

    def get_carrier(self):
        return self.carrier

    def set_carrier(self, carrier):
        self.carrier = carrier
        self.uhd_usrp_sink_0.set_center_freq(self.carrier, 0)
        self.uhd_usrp_sink_0.set_center_freq(self.carrier, 1)
        self.uhd_usrp_sink_0.set_center_freq(self.carrier, 2)
        self.uhd_usrp_sink_0.set_center_freq(self.carrier, 3)


def main(top_block_cls=tutorial_two_1, options=None):

    tb = top_block_cls()
    tb.start()
    tb.wait()


if __name__ == '__main__':
    main()
