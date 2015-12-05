#!/usr/bin/env python2
##################################################
# GNU Radio Python Flow Graph
# Title: Top Block
# Generated: Fri Dec  4 19:29:42 2015
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
from gnuradio import analog
from gnuradio import audio
from gnuradio import blocks
from gnuradio import eng_notation
from gnuradio import filter
from gnuradio import gr
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from gnuradio.qtgui import Range, RangeWidget
from optparse import OptionParser
import sys


class top_block(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "Top Block")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Top Block")
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

        self.settings = Qt.QSettings("GNU Radio", "top_block")
        self.restoreGeometry(self.settings.value("geometry").toByteArray())

        ##################################################
        # Variables
        ##################################################
        self.samp_rate = samp_rate = 44100
        self.center1 = center1 = 0

        ##################################################
        # Blocks
        ##################################################
        self._center1_range = Range(-20000, 20000, 100, 0, 200)
        self._center1_win = RangeWidget(self._center1_range, self.set_center1, "center1", "counter_slider", float)
        self.top_layout.addWidget(self._center1_win)
        self.freq_xlating_fir_filter_xxx_0 = filter.freq_xlating_fir_filter_fcf(1, (1, ), center1, samp_rate)
        self.freq_xlating_fft_filter_ccc_0 = filter.freq_xlating_fft_filter_ccc(1, (1, ), center1, samp_rate)
        self.freq_xlating_fft_filter_ccc_0.set_nthreads(1)
        self.freq_xlating_fft_filter_ccc_0.declare_sample_delay(0)
        self.blocks_float_to_complex_0 = blocks.float_to_complex(1)
        self.blocks_complex_to_float_0_0 = blocks.complex_to_float(1)
        self.blocks_complex_to_float_0 = blocks.complex_to_float(1)
        self.audio_source_0 = audio.source(samp_rate, "", True)
        self.audio_sink_0 = audio.sink(samp_rate, "", True)
        self.analog_const_source_x_0 = analog.sig_source_f(0, analog.GR_CONST_WAVE, 0, 0, 0)

        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_const_source_x_0, 0), (self.blocks_float_to_complex_0, 1))    
        self.connect((self.audio_source_0, 0), (self.blocks_float_to_complex_0, 0))    
        self.connect((self.audio_source_0, 0), (self.freq_xlating_fir_filter_xxx_0, 0))    
        self.connect((self.blocks_complex_to_float_0, 0), (self.audio_sink_0, 0))    
        self.connect((self.blocks_complex_to_float_0_0, 0), (self.audio_sink_0, 1))    
        self.connect((self.blocks_float_to_complex_0, 0), (self.freq_xlating_fft_filter_ccc_0, 0))    
        self.connect((self.freq_xlating_fft_filter_ccc_0, 0), (self.blocks_complex_to_float_0_0, 0))    
        self.connect((self.freq_xlating_fir_filter_xxx_0, 0), (self.blocks_complex_to_float_0, 0))    

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "top_block")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate

    def get_center1(self):
        return self.center1

    def set_center1(self, center1):
        self.center1 = center1
        self.freq_xlating_fft_filter_ccc_0.set_center_freq(self.center1)
        self.freq_xlating_fir_filter_xxx_0.set_center_freq(self.center1)


if __name__ == '__main__':
    parser = OptionParser(option_class=eng_option, usage="%prog: [options]")
    (options, args) = parser.parse_args()
    from distutils.version import StrictVersion
    if StrictVersion(Qt.qVersion()) >= StrictVersion("4.5.0"):
        Qt.QApplication.setGraphicsSystem(gr.prefs().get_string('qtgui','style','raster'))
    qapp = Qt.QApplication(sys.argv)
    tb = top_block()
    tb.start()
    tb.show()

    def quitting():
        tb.stop()
        tb.wait()
    qapp.connect(qapp, Qt.SIGNAL("aboutToQuit()"), quitting)
    qapp.exec_()
    tb = None  # to clean up Qt widgets
