#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Playfile
# GNU Radio version: 3.7.13.5
##################################################

if __name__ == '__main__':
    import ctypes
    import sys
    if sys.platform.startswith('linux'):
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print "Warning: failed to XInitThreads()"

from PyQt4 import Qt
from gnuradio import blocks
from gnuradio import eng_notation
from gnuradio import gr
from gnuradio import uhd
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from gnuradio.qtgui import Range, RangeWidget
from optparse import OptionParser
import pmt
import sys
import time
from gnuradio import qtgui


class PlayFile(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "Playfile")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Playfile")
        qtgui.util.check_set_qss()
        try:
            self.setWindowIcon(Qt.QIcon.fromTheme('gnuradio-grc'))
        except:
            pass
        self.top_scroll_layout = Qt.QVBoxLayout()
        self.setLayout(self.top_scroll_layout)
        self.top_scroll = Qt.QScrollArea()
        self.top_scroll.setFrameStyle(Qt.QFrame.NoFrame)
        self.top_scroll_layout.addWidget(self.top_scroll)
        self.top_scroll.setWidgetResizable(True)
        self.top_widget = Qt.QWidget()
        self.top_scroll.setWidget(self.top_widget)
        self.top_layout = Qt.QVBoxLayout(self.top_widget)
        self.top_grid_layout = Qt.QGridLayout()
        self.top_layout.addLayout(self.top_grid_layout)

        self.settings = Qt.QSettings("GNU Radio", "PlayFile")
        self.restoreGeometry(self.settings.value("geometry").toByteArray())


        ##################################################
        # Variables
        ##################################################
        self.txgain = txgain = 0
        self.samp_rate = samp_rate = 1.25e6/5
        self.carrier = carrier = 900000000

        ##################################################
        # Blocks
        ##################################################
        self._txgain_range = Range(-20, 50, 1, 0, 200)
        self._txgain_win = RangeWidget(self._txgain_range, self.set_txgain, "txgain", "counter_slider", float)
        self.top_grid_layout.addWidget(self._txgain_win)
        self.uhd_usrp_sink_0 = uhd.usrp_sink(
        	",".join(("addr=192.168.10.2", "")),
        	uhd.stream_args(
        		cpu_format="fc32",
        		channels=range(4),
        	),
        )
        self.uhd_usrp_sink_0.set_samp_rate(samp_rate)
        self.uhd_usrp_sink_0.set_center_freq(carrier, 0)
        self.uhd_usrp_sink_0.set_gain(txgain, 0)
        self.uhd_usrp_sink_0.set_antenna('TX/RX', 0)
        self.uhd_usrp_sink_0.set_center_freq(carrier, 1)
        self.uhd_usrp_sink_0.set_gain(txgain, 1)
        self.uhd_usrp_sink_0.set_antenna('TX/RX', 1)
        self.uhd_usrp_sink_0.set_center_freq(carrier, 2)
        self.uhd_usrp_sink_0.set_gain(txgain, 2)
        self.uhd_usrp_sink_0.set_antenna('TX/RX', 2)
        self.uhd_usrp_sink_0.set_center_freq(carrier, 3)
        self.uhd_usrp_sink_0.set_gain(txgain, 3)
        self.uhd_usrp_sink_0.set_antenna('TX/RX', 3)
        self.blocks_null_source_0_0 = blocks.null_source(gr.sizeof_gr_complex*1)
        self.blocks_null_source_0 = blocks.null_source(gr.sizeof_gr_complex*1)
        self.blocks_head_0 = blocks.head(gr.sizeof_gr_complex*1, 1250000*1000)
        self.blocks_float_to_complex_0 = blocks.float_to_complex(1)
        self.blocks_file_source_0_0 = blocks.file_source(gr.sizeof_float*1, '/home/venkatesh/Desktop/USRPProject/DataCollect/IQSamples/Transmit/18thAugustCorrectScalingNoSNRSetNoChannelEffects/64QAM18thAug2019EvenImag.bin', True)
        self.blocks_file_source_0_0.set_begin_tag(pmt.PMT_NIL)
        self.blocks_file_source_0 = blocks.file_source(gr.sizeof_float*1, '/home/venkatesh/Desktop/USRPProject/DataCollect/IQSamples/Transmit/18thAugustCorrectScalingNoSNRSetNoChannelEffects/64QAM18thAug2019EvenReal.bin', True)
        self.blocks_file_source_0.set_begin_tag(pmt.PMT_NIL)



        ##################################################
        # Connections
        ##################################################
        self.connect((self.blocks_file_source_0, 0), (self.blocks_float_to_complex_0, 0))
        self.connect((self.blocks_file_source_0_0, 0), (self.blocks_float_to_complex_0, 1))
        self.connect((self.blocks_float_to_complex_0, 0), (self.blocks_head_0, 0))
        self.connect((self.blocks_head_0, 0), (self.uhd_usrp_sink_0, 0))
        self.connect((self.blocks_head_0, 0), (self.uhd_usrp_sink_0, 1))
        self.connect((self.blocks_null_source_0, 0), (self.uhd_usrp_sink_0, 2))
        self.connect((self.blocks_null_source_0_0, 0), (self.uhd_usrp_sink_0, 3))

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "PlayFile")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_txgain(self):
        return self.txgain

    def set_txgain(self, txgain):
        self.txgain = txgain
        self.uhd_usrp_sink_0.set_gain(self.txgain, 0)

        self.uhd_usrp_sink_0.set_gain(self.txgain, 1)

        self.uhd_usrp_sink_0.set_gain(self.txgain, 2)

        self.uhd_usrp_sink_0.set_gain(self.txgain, 3)


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


def main(top_block_cls=PlayFile, options=None):

    from distutils.version import StrictVersion
    if StrictVersion(Qt.qVersion()) >= StrictVersion("4.5.0"):
        style = gr.prefs().get_string('qtgui', 'style', 'raster')
        Qt.QApplication.setGraphicsSystem(style)
    qapp = Qt.QApplication(sys.argv)

    tb = top_block_cls()
    tb.start()
    tb.show()

    def quitting():
        tb.stop()
        tb.wait()
    qapp.connect(qapp, Qt.SIGNAL("aboutToQuit()"), quitting)
    qapp.exec_()


if __name__ == '__main__':
    main()
