#!/usr/bin/env python2
##################################################
# GNU Radio Python Flow Graph
# Title: Bander: Shift Bands around
# Generated: Sat Nov 28 18:11:14 2015
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


class bander3(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "Bander: Shift Bands around")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Bander: Shift Bands around")
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

        self.settings = Qt.QSettings("GNU Radio", "bander3")
        self.restoreGeometry(self.settings.value("geometry").toByteArray())

        ##################################################
        # Variables
        ##################################################
        self.transition = transition = 100
        self.transcenter = transcenter = 2000
        self.samp_rate = samp_rate = 48000
        self.xlatecenter4 = xlatecenter4 = 0
        self.xlatecenter3 = xlatecenter3 = 0
        self.xlatecenter2 = xlatecenter2 = 0
        self.xlatecenter1 = xlatecenter1 = 0
        self.xlate = xlate = firdes.low_pass(1, samp_rate, transcenter, transition, firdes.WIN_HAMMING, 6.76)
        self.decayrate = decayrate = 0.01
        self.bptrans = bptrans = 300
        self.bplow_4 = bplow_4 = 1
        self.bplow_3 = bplow_3 = 1
        self.bplow_2 = bplow_2 = 1
        self.bplow_1 = bplow_1 = 1
        self.bphi_4 = bphi_4 = 2800
        self.bphi_3 = bphi_3 = 2800
        self.bphi_2 = bphi_2 = 2800
        self.bphi_1 = bphi_1 = 2800
        self.atkrate = atkrate = 0.1

        ##################################################
        # Blocks
        ##################################################
        self._xlatecenter4_range = Range(-12000, 12000, 10, 0, 200)
        self._xlatecenter4_win = RangeWidget(self._xlatecenter4_range, self.set_xlatecenter4, "xlatecenter4", "counter_slider", float)
        self.top_layout.addWidget(self._xlatecenter4_win)
        self._xlatecenter3_range = Range(-12000, 12000, 10, 0, 200)
        self._xlatecenter3_win = RangeWidget(self._xlatecenter3_range, self.set_xlatecenter3, "xlatecenter3", "counter_slider", float)
        self.top_layout.addWidget(self._xlatecenter3_win)
        self._xlatecenter2_range = Range(-12000, 12000, 10, 0, 200)
        self._xlatecenter2_win = RangeWidget(self._xlatecenter2_range, self.set_xlatecenter2, "xlatecenter2", "counter_slider", float)
        self.top_layout.addWidget(self._xlatecenter2_win)
        self._xlatecenter1_range = Range(-12000, 12000, 10, 0, 200)
        self._xlatecenter1_win = RangeWidget(self._xlatecenter1_range, self.set_xlatecenter1, "xlatecenter1", "counter_slider", float)
        self.top_layout.addWidget(self._xlatecenter1_win)
        self._bptrans_range = Range(0, 1000, 1, 300, 200)
        self._bptrans_win = RangeWidget(self._bptrans_range, self.set_bptrans, "BP-Trans", "counter_slider", float)
        self.top_layout.addWidget(self._bptrans_win)
        self._bplow_4_range = Range(1, 1000, 1, 1, 200)
        self._bplow_4_win = RangeWidget(self._bplow_4_range, self.set_bplow_4, "BP-Low-4", "counter_slider", float)
        self.top_layout.addWidget(self._bplow_4_win)
        self._bplow_3_range = Range(1, 1000, 1, 1, 200)
        self._bplow_3_win = RangeWidget(self._bplow_3_range, self.set_bplow_3, "BP-Low-3", "counter_slider", float)
        self.top_layout.addWidget(self._bplow_3_win)
        self._bplow_2_range = Range(1, 1000, 1, 1, 200)
        self._bplow_2_win = RangeWidget(self._bplow_2_range, self.set_bplow_2, "BP-Low-2", "counter_slider", float)
        self.top_layout.addWidget(self._bplow_2_win)
        self._bplow_1_range = Range(1, 1000, 1, 1, 200)
        self._bplow_1_win = RangeWidget(self._bplow_1_range, self.set_bplow_1, "BP-Low-1", "counter_slider", float)
        self.top_layout.addWidget(self._bplow_1_win)
        self._bphi_4_range = Range(0, 5000, 10, 2800, 200)
        self._bphi_4_win = RangeWidget(self._bphi_4_range, self.set_bphi_4, "BP-Hi-4", "counter_slider", float)
        self.top_layout.addWidget(self._bphi_4_win)
        self._bphi_3_range = Range(0, 5000, 10, 2800, 200)
        self._bphi_3_win = RangeWidget(self._bphi_3_range, self.set_bphi_3, "BP-Hi-3", "counter_slider", float)
        self.top_layout.addWidget(self._bphi_3_win)
        self._bphi_2_range = Range(0, 5000, 10, 2800, 200)
        self._bphi_2_win = RangeWidget(self._bphi_2_range, self.set_bphi_2, "BP-Hi-2", "counter_slider", float)
        self.top_layout.addWidget(self._bphi_2_win)
        self._bphi_1_range = Range(0, 5000, 10, 2800, 200)
        self._bphi_1_win = RangeWidget(self._bphi_1_range, self.set_bphi_1, "BP-Hi-1", "counter_slider", float)
        self.top_layout.addWidget(self._bphi_1_win)
        self._transition_range = Range(0, 8000, 10, 100, 200)
        self._transition_win = RangeWidget(self._transition_range, self.set_transition, "Transition Band", "counter_slider", float)
        self.top_layout.addWidget(self._transition_win)
        self._transcenter_range = Range(0, 8000, 10, 2000, 200)
        self._transcenter_win = RangeWidget(self._transcenter_range, self.set_transcenter, "Transition Center", "counter_slider", float)
        self.top_layout.addWidget(self._transcenter_win)
        self.freq_xlating_fir_filter_xxx_0_0_1 = filter.freq_xlating_fir_filter_fcc(1, (xlate), xlatecenter4, samp_rate)
        self.freq_xlating_fir_filter_xxx_0_0_0 = filter.freq_xlating_fir_filter_fcc(1, (xlate), xlatecenter3, samp_rate)
        self.freq_xlating_fir_filter_xxx_0_0 = filter.freq_xlating_fir_filter_fcc(1, (xlate), xlatecenter2, samp_rate)
        self.freq_xlating_fir_filter_xxx_0 = filter.freq_xlating_fir_filter_fcc(1, (xlate), xlatecenter1, samp_rate)
        self._decayrate_range = Range(0, 2, 0.01, 0.01, 200)
        self._decayrate_win = RangeWidget(self._decayrate_range, self.set_decayrate, "Decay Rate", "counter_slider", float)
        self.top_layout.addWidget(self._decayrate_win)
        self.blocks_complex_to_mag_0_0_1 = blocks.complex_to_mag(1)
        self.blocks_complex_to_mag_0_0_0 = blocks.complex_to_mag(1)
        self.blocks_complex_to_mag_0_0 = blocks.complex_to_mag(1)
        self.blocks_complex_to_mag_0 = blocks.complex_to_mag(1)
        self.band_pass_filter_0_0_0_0 = filter.fir_filter_ccf(1, firdes.band_pass(
        	1, samp_rate, bplow_4, bphi_4, bptrans, firdes.WIN_HAMMING, 6.76))
        self.band_pass_filter_0_0_0 = filter.fir_filter_ccf(1, firdes.band_pass(
        	1, samp_rate, bplow_3, bphi_3, bptrans, firdes.WIN_HAMMING, 6.76))
        self.band_pass_filter_0_0 = filter.fir_filter_ccf(1, firdes.band_pass(
        	1, samp_rate, bplow_2, bphi_2, bptrans, firdes.WIN_HAMMING, 6.76))
        self.band_pass_filter_0 = filter.fir_filter_ccf(1, firdes.band_pass(
        	1, samp_rate, bplow_1, bphi_1, bptrans, firdes.WIN_HAMMING, 6.76))
        self.audio_source_0 = audio.source(samp_rate, "Bander:input", True)
        self.audio_sink_0_0_1 = audio.sink(samp_rate, "Bander:4", True)
        self.audio_sink_0_0_0 = audio.sink(samp_rate, "Bander:3", True)
        self.audio_sink_0_0 = audio.sink(samp_rate, "Bander:2", True)
        self.audio_sink_0 = audio.sink(samp_rate, "Bander:1", True)
        self._atkrate_range = Range(0, 2, 0.01, 0.1, 200)
        self._atkrate_win = RangeWidget(self._atkrate_range, self.set_atkrate, "Attack Rate", "counter_slider", float)
        self.top_layout.addWidget(self._atkrate_win)

        ##################################################
        # Connections
        ##################################################
        self.connect((self.audio_source_0, 0), (self.freq_xlating_fir_filter_xxx_0, 0))    
        self.connect((self.audio_source_0, 0), (self.freq_xlating_fir_filter_xxx_0_0, 0))    
        self.connect((self.audio_source_0, 0), (self.freq_xlating_fir_filter_xxx_0_0_0, 0))    
        self.connect((self.audio_source_0, 0), (self.freq_xlating_fir_filter_xxx_0_0_1, 0))    
        self.connect((self.band_pass_filter_0, 0), (self.blocks_complex_to_mag_0, 0))    
        self.connect((self.band_pass_filter_0_0, 0), (self.blocks_complex_to_mag_0_0, 0))    
        self.connect((self.band_pass_filter_0_0_0, 0), (self.blocks_complex_to_mag_0_0_0, 0))    
        self.connect((self.band_pass_filter_0_0_0_0, 0), (self.blocks_complex_to_mag_0_0_1, 0))    
        self.connect((self.blocks_complex_to_mag_0, 0), (self.audio_sink_0, 0))    
        self.connect((self.blocks_complex_to_mag_0_0, 0), (self.audio_sink_0_0, 0))    
        self.connect((self.blocks_complex_to_mag_0_0_0, 0), (self.audio_sink_0_0_0, 0))    
        self.connect((self.blocks_complex_to_mag_0_0_1, 0), (self.audio_sink_0_0_1, 0))    
        self.connect((self.freq_xlating_fir_filter_xxx_0, 0), (self.band_pass_filter_0, 0))    
        self.connect((self.freq_xlating_fir_filter_xxx_0_0, 0), (self.band_pass_filter_0_0, 0))    
        self.connect((self.freq_xlating_fir_filter_xxx_0_0_0, 0), (self.band_pass_filter_0_0_0, 0))    
        self.connect((self.freq_xlating_fir_filter_xxx_0_0_1, 0), (self.band_pass_filter_0_0_0_0, 0))    

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "bander3")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_transition(self):
        return self.transition

    def set_transition(self, transition):
        self.transition = transition
        self.set_xlate(firdes.low_pass(1, self.samp_rate, self.transcenter, self.transition, firdes.WIN_HAMMING, 6.76))

    def get_transcenter(self):
        return self.transcenter

    def set_transcenter(self, transcenter):
        self.transcenter = transcenter
        self.set_xlate(firdes.low_pass(1, self.samp_rate, self.transcenter, self.transition, firdes.WIN_HAMMING, 6.76))

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.set_xlate(firdes.low_pass(1, self.samp_rate, self.transcenter, self.transition, firdes.WIN_HAMMING, 6.76))
        self.band_pass_filter_0.set_taps(firdes.band_pass(1, self.samp_rate, self.bplow_1, self.bphi_1, self.bptrans, firdes.WIN_HAMMING, 6.76))
        self.band_pass_filter_0_0.set_taps(firdes.band_pass(1, self.samp_rate, self.bplow_2, self.bphi_2, self.bptrans, firdes.WIN_HAMMING, 6.76))
        self.band_pass_filter_0_0_0.set_taps(firdes.band_pass(1, self.samp_rate, self.bplow_3, self.bphi_3, self.bptrans, firdes.WIN_HAMMING, 6.76))
        self.band_pass_filter_0_0_0_0.set_taps(firdes.band_pass(1, self.samp_rate, self.bplow_4, self.bphi_4, self.bptrans, firdes.WIN_HAMMING, 6.76))

    def get_xlatecenter4(self):
        return self.xlatecenter4

    def set_xlatecenter4(self, xlatecenter4):
        self.xlatecenter4 = xlatecenter4
        self.freq_xlating_fir_filter_xxx_0_0_1.set_center_freq(self.xlatecenter4)

    def get_xlatecenter3(self):
        return self.xlatecenter3

    def set_xlatecenter3(self, xlatecenter3):
        self.xlatecenter3 = xlatecenter3
        self.freq_xlating_fir_filter_xxx_0_0_0.set_center_freq(self.xlatecenter3)

    def get_xlatecenter2(self):
        return self.xlatecenter2

    def set_xlatecenter2(self, xlatecenter2):
        self.xlatecenter2 = xlatecenter2
        self.freq_xlating_fir_filter_xxx_0_0.set_center_freq(self.xlatecenter2)

    def get_xlatecenter1(self):
        return self.xlatecenter1

    def set_xlatecenter1(self, xlatecenter1):
        self.xlatecenter1 = xlatecenter1
        self.freq_xlating_fir_filter_xxx_0.set_center_freq(self.xlatecenter1)

    def get_xlate(self):
        return self.xlate

    def set_xlate(self, xlate):
        self.xlate = xlate
        self.freq_xlating_fir_filter_xxx_0.set_taps((self.xlate))
        self.freq_xlating_fir_filter_xxx_0_0.set_taps((self.xlate))
        self.freq_xlating_fir_filter_xxx_0_0_0.set_taps((self.xlate))
        self.freq_xlating_fir_filter_xxx_0_0_1.set_taps((self.xlate))

    def get_decayrate(self):
        return self.decayrate

    def set_decayrate(self, decayrate):
        self.decayrate = decayrate

    def get_bptrans(self):
        return self.bptrans

    def set_bptrans(self, bptrans):
        self.bptrans = bptrans
        self.band_pass_filter_0.set_taps(firdes.band_pass(1, self.samp_rate, self.bplow_1, self.bphi_1, self.bptrans, firdes.WIN_HAMMING, 6.76))
        self.band_pass_filter_0_0.set_taps(firdes.band_pass(1, self.samp_rate, self.bplow_2, self.bphi_2, self.bptrans, firdes.WIN_HAMMING, 6.76))
        self.band_pass_filter_0_0_0.set_taps(firdes.band_pass(1, self.samp_rate, self.bplow_3, self.bphi_3, self.bptrans, firdes.WIN_HAMMING, 6.76))
        self.band_pass_filter_0_0_0_0.set_taps(firdes.band_pass(1, self.samp_rate, self.bplow_4, self.bphi_4, self.bptrans, firdes.WIN_HAMMING, 6.76))

    def get_bplow_4(self):
        return self.bplow_4

    def set_bplow_4(self, bplow_4):
        self.bplow_4 = bplow_4
        self.band_pass_filter_0_0_0_0.set_taps(firdes.band_pass(1, self.samp_rate, self.bplow_4, self.bphi_4, self.bptrans, firdes.WIN_HAMMING, 6.76))

    def get_bplow_3(self):
        return self.bplow_3

    def set_bplow_3(self, bplow_3):
        self.bplow_3 = bplow_3
        self.band_pass_filter_0_0_0.set_taps(firdes.band_pass(1, self.samp_rate, self.bplow_3, self.bphi_3, self.bptrans, firdes.WIN_HAMMING, 6.76))

    def get_bplow_2(self):
        return self.bplow_2

    def set_bplow_2(self, bplow_2):
        self.bplow_2 = bplow_2
        self.band_pass_filter_0_0.set_taps(firdes.band_pass(1, self.samp_rate, self.bplow_2, self.bphi_2, self.bptrans, firdes.WIN_HAMMING, 6.76))

    def get_bplow_1(self):
        return self.bplow_1

    def set_bplow_1(self, bplow_1):
        self.bplow_1 = bplow_1
        self.band_pass_filter_0.set_taps(firdes.band_pass(1, self.samp_rate, self.bplow_1, self.bphi_1, self.bptrans, firdes.WIN_HAMMING, 6.76))

    def get_bphi_4(self):
        return self.bphi_4

    def set_bphi_4(self, bphi_4):
        self.bphi_4 = bphi_4
        self.band_pass_filter_0_0_0_0.set_taps(firdes.band_pass(1, self.samp_rate, self.bplow_4, self.bphi_4, self.bptrans, firdes.WIN_HAMMING, 6.76))

    def get_bphi_3(self):
        return self.bphi_3

    def set_bphi_3(self, bphi_3):
        self.bphi_3 = bphi_3
        self.band_pass_filter_0_0_0.set_taps(firdes.band_pass(1, self.samp_rate, self.bplow_3, self.bphi_3, self.bptrans, firdes.WIN_HAMMING, 6.76))

    def get_bphi_2(self):
        return self.bphi_2

    def set_bphi_2(self, bphi_2):
        self.bphi_2 = bphi_2
        self.band_pass_filter_0_0.set_taps(firdes.band_pass(1, self.samp_rate, self.bplow_2, self.bphi_2, self.bptrans, firdes.WIN_HAMMING, 6.76))

    def get_bphi_1(self):
        return self.bphi_1

    def set_bphi_1(self, bphi_1):
        self.bphi_1 = bphi_1
        self.band_pass_filter_0.set_taps(firdes.band_pass(1, self.samp_rate, self.bplow_1, self.bphi_1, self.bptrans, firdes.WIN_HAMMING, 6.76))

    def get_atkrate(self):
        return self.atkrate

    def set_atkrate(self, atkrate):
        self.atkrate = atkrate


if __name__ == '__main__':
    parser = OptionParser(option_class=eng_option, usage="%prog: [options]")
    (options, args) = parser.parse_args()
    from distutils.version import StrictVersion
    if StrictVersion(Qt.qVersion()) >= StrictVersion("4.5.0"):
        Qt.QApplication.setGraphicsSystem(gr.prefs().get_string('qtgui','style','raster'))
    qapp = Qt.QApplication(sys.argv)
    tb = bander3()
    tb.start()
    tb.show()

    def quitting():
        tb.stop()
        tb.wait()
    qapp.connect(qapp, Qt.SIGNAL("aboutToQuit()"), quitting)
    qapp.exec_()
    tb = None  # to clean up Qt widgets
