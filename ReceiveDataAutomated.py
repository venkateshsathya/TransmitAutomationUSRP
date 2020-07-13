#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Receivedataautomated
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
from gnuradio import qtgui
from gnuradio import uhd
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from optparse import OptionParser
import sip
import sys
import time
from gnuradio import qtgui


class ReceiveDataAutomated(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "Receivedataautomated")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Receivedataautomated")
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

        self.settings = Qt.QSettings("GNU Radio", "ReceiveDataAutomated")
        self.restoreGeometry(self.settings.value("geometry").toByteArray())


        ##################################################
        # Variables
        ##################################################
        self.samp_rate = samp_rate = 125000000/500
        self.carrier = carrier = 1500000000
        self.RXGainSlider = RXGainSlider = 18
        self.NumSeconds = NumSeconds = 10000

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
        self.qtgui_const_sink_x_0_2 = qtgui.const_sink_c(
        	8192, #size
        	"", #name
        	1 #number of inputs
        )
        self.qtgui_const_sink_x_0_2.set_update_time(0.10)
        self.qtgui_const_sink_x_0_2.set_y_axis(-2, 2)
        self.qtgui_const_sink_x_0_2.set_x_axis(-2, 2)
        self.qtgui_const_sink_x_0_2.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, "")
        self.qtgui_const_sink_x_0_2.enable_autoscale(True)
        self.qtgui_const_sink_x_0_2.enable_grid(False)
        self.qtgui_const_sink_x_0_2.enable_axis_labels(True)

        if not True:
          self.qtgui_const_sink_x_0_2.disable_legend()

        labels = ['', '', '', '', '',
                  '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "red", "red", "red",
                  "red", "red", "red", "red", "red"]
        styles = [0, 0, 0, 0, 0,
                  0, 0, 0, 0, 0]
        markers = [0, 0, 0, 0, 0,
                   0, 0, 0, 0, 0]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        for i in xrange(1):
            if len(labels[i]) == 0:
                self.qtgui_const_sink_x_0_2.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_const_sink_x_0_2.set_line_label(i, labels[i])
            self.qtgui_const_sink_x_0_2.set_line_width(i, widths[i])
            self.qtgui_const_sink_x_0_2.set_line_color(i, colors[i])
            self.qtgui_const_sink_x_0_2.set_line_style(i, styles[i])
            self.qtgui_const_sink_x_0_2.set_line_marker(i, markers[i])
            self.qtgui_const_sink_x_0_2.set_line_alpha(i, alphas[i])

        self._qtgui_const_sink_x_0_2_win = sip.wrapinstance(self.qtgui_const_sink_x_0_2.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_const_sink_x_0_2_win)
        self.qtgui_const_sink_x_0_1 = qtgui.const_sink_c(
        	8192, #size
        	"", #name
        	1 #number of inputs
        )
        self.qtgui_const_sink_x_0_1.set_update_time(0.10)
        self.qtgui_const_sink_x_0_1.set_y_axis(-2, 2)
        self.qtgui_const_sink_x_0_1.set_x_axis(-2, 2)
        self.qtgui_const_sink_x_0_1.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, "")
        self.qtgui_const_sink_x_0_1.enable_autoscale(True)
        self.qtgui_const_sink_x_0_1.enable_grid(False)
        self.qtgui_const_sink_x_0_1.enable_axis_labels(True)

        if not True:
          self.qtgui_const_sink_x_0_1.disable_legend()

        labels = ['', '', '', '', '',
                  '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "red", "red", "red",
                  "red", "red", "red", "red", "red"]
        styles = [0, 0, 0, 0, 0,
                  0, 0, 0, 0, 0]
        markers = [0, 0, 0, 0, 0,
                   0, 0, 0, 0, 0]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        for i in xrange(1):
            if len(labels[i]) == 0:
                self.qtgui_const_sink_x_0_1.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_const_sink_x_0_1.set_line_label(i, labels[i])
            self.qtgui_const_sink_x_0_1.set_line_width(i, widths[i])
            self.qtgui_const_sink_x_0_1.set_line_color(i, colors[i])
            self.qtgui_const_sink_x_0_1.set_line_style(i, styles[i])
            self.qtgui_const_sink_x_0_1.set_line_marker(i, markers[i])
            self.qtgui_const_sink_x_0_1.set_line_alpha(i, alphas[i])

        self._qtgui_const_sink_x_0_1_win = sip.wrapinstance(self.qtgui_const_sink_x_0_1.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_const_sink_x_0_1_win)
        self.qtgui_const_sink_x_0 = qtgui.const_sink_c(
        	8192, #size
        	"", #name
        	1 #number of inputs
        )
        self.qtgui_const_sink_x_0.set_update_time(0.10)
        self.qtgui_const_sink_x_0.set_y_axis(-2, 2)
        self.qtgui_const_sink_x_0.set_x_axis(-2, 2)
        self.qtgui_const_sink_x_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, "")
        self.qtgui_const_sink_x_0.enable_autoscale(True)
        self.qtgui_const_sink_x_0.enable_grid(False)
        self.qtgui_const_sink_x_0.enable_axis_labels(True)

        if not True:
          self.qtgui_const_sink_x_0.disable_legend()

        labels = ['', '', '', '', '',
                  '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "red", "red", "red",
                  "red", "red", "red", "red", "red"]
        styles = [0, 0, 0, 0, 0,
                  0, 0, 0, 0, 0]
        markers = [0, 0, 0, 0, 0,
                   0, 0, 0, 0, 0]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        for i in xrange(1):
            if len(labels[i]) == 0:
                self.qtgui_const_sink_x_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_const_sink_x_0.set_line_label(i, labels[i])
            self.qtgui_const_sink_x_0.set_line_width(i, widths[i])
            self.qtgui_const_sink_x_0.set_line_color(i, colors[i])
            self.qtgui_const_sink_x_0.set_line_style(i, styles[i])
            self.qtgui_const_sink_x_0.set_line_marker(i, markers[i])
            self.qtgui_const_sink_x_0.set_line_alpha(i, alphas[i])

        self._qtgui_const_sink_x_0_win = sip.wrapinstance(self.qtgui_const_sink_x_0.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_const_sink_x_0_win)
        self.blocks_head_0_2 = blocks.head(gr.sizeof_gr_complex*1, NumSeconds*samp_rate)
        self.blocks_head_0_1 = blocks.head(gr.sizeof_gr_complex*1, NumSeconds*samp_rate)
        self.blocks_head_0_0 = blocks.head(gr.sizeof_gr_complex*1, NumSeconds*samp_rate)
        self.blocks_head_0 = blocks.head(gr.sizeof_gr_complex*1, NumSeconds*samp_rate)
        self.blocks_file_sink_0_0_0_0 = blocks.file_sink(gr.sizeof_gr_complex*1, '/home/venkatesh/Desktop/USRPProject/DataCollect/16QAMCorrectScaleChain1Aug19_1.bin', False)
        self.blocks_file_sink_0_0_0_0.set_unbuffered(False)
        self.blocks_file_sink_0_0_0 = blocks.file_sink(gr.sizeof_gr_complex*1, '/home/venkatesh/Desktop/USRPProject/DataCollect/16QAMCorrectScaleChain2Aug19_1.bin', False)
        self.blocks_file_sink_0_0_0.set_unbuffered(False)
        self.blocks_file_sink_0_0 = blocks.file_sink(gr.sizeof_gr_complex*1, '/home/venkatesh/Desktop/USRPProject/DataCollect/QPSKCorrectScaleChain4Aug19_1.bin', False)
        self.blocks_file_sink_0_0.set_unbuffered(False)
        self.blocks_file_sink_0 = blocks.file_sink(gr.sizeof_gr_complex*1, '/home/venkatesh/Desktop/USRPProject/DataCollect/16QAMCorrectScaleChain3Aug19_1.bin', False)
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
        self.connect((self.uhd_usrp_source_0, 1), (self.qtgui_const_sink_x_0, 0))
        self.connect((self.uhd_usrp_source_0, 2), (self.qtgui_const_sink_x_0_1, 0))
        self.connect((self.uhd_usrp_source_0, 3), (self.qtgui_const_sink_x_0_2, 0))

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "ReceiveDataAutomated")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

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
