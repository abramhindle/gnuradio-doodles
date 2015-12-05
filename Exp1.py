#!/usr/bin/env python2
##################################################
# GNU Radio Python Flow Graph
# Title: FM radio FFT example
# Author: David Haworth, Abram Hindle
# Generated: Fri Dec  4 20:04:18 2015
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
import osmosdr
import sys
import time


class Exp1(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "FM radio FFT example")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("FM radio FFT example")
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

        self.settings = Qt.QSettings("GNU Radio", "Exp1")
        self.restoreGeometry(self.settings.value("geometry").toByteArray())

        ##################################################
        # Variables
        ##################################################
        self.variable_sample_rate_0 = variable_sample_rate_0 = 1e6
        self.samp_rate = samp_rate = 44100
        self.xlatecenter_4 = xlatecenter_4 = 0
        self.xlatecenter_3 = xlatecenter_3 = 0
        self.xlatecenter_2 = xlatecenter_2 = 0
        self.xlatecenter = xlatecenter = 0
        self.xlate_filter2 = xlate_filter2 = firdes.low_pass(1, samp_rate, 4000, 1000, firdes.WIN_HAMMING, 6.76)
        self.xlate_filter = xlate_filter = firdes.low_pass(1, variable_sample_rate_0, 125000, 25000, firdes.WIN_HAMMING, 6.76)
        self.variable_1 = variable_1 = 0
        self.transition = transition = 1e6
        self.rri = rri = 441
        self.rrd = rrd = 500
        self.quadrature = quadrature = 500000
        self.pscf4 = pscf4 = 0
        self.pscf3 = pscf3 = 0
        self.pscf2 = pscf2 = 0
        self.pscf1 = pscf1 = 0
        self.cutoff = cutoff = 1e5
        self.bptrans = bptrans = 100
        self.bpsr = bpsr = 200000
        self.bplow_4 = bplow_4 = 100
        self.bplow_3 = bplow_3 = 100
        self.bplow_2 = bplow_2 = 100
        self.bplow_1 = bplow_1 = 100
        self.bphi_4 = bphi_4 = 2.8e3
        self.bphi_3 = bphi_3 = 2.8e3
        self.bphi_2 = bphi_2 = 2.8e3
        self.bphi_1 = bphi_1 = 2.8e3
        self.audio_interp = audio_interp = 4
        self.amp_4 = amp_4 = 0
        self.amp_3 = amp_3 = 0
        self.amp_2 = amp_2 = 0
        self.amp_1 = amp_1 = 1
        self.RF_Gain = RF_Gain = 35
        self.CF = CF = 88.5e6

        ##################################################
        # Blocks
        ##################################################
        self._pscf1_range = Range(-10000, 10000, 50, 0, 200)
        self._pscf1_win = RangeWidget(self._pscf1_range, self.set_pscf1, "pscf1", "counter_slider", float)
        self.top_layout.addWidget(self._pscf1_win)
        self._amp_1_range = Range(0, 1, 0.01, 1, 200)
        self._amp_1_win = RangeWidget(self._amp_1_range, self.set_amp_1, "Amp", "counter_slider", float)
        self.top_layout.addWidget(self._amp_1_win)
        self.rational_resampler_xxx_1_0_0 = filter.rational_resampler_ccc(
                interpolation=rri,
                decimation=rrd,
                taps=None,
                fractional_bw=None,
        )
        self.rational_resampler_xxx_1_0 = filter.rational_resampler_fff(
                interpolation=rri,
                decimation=rrd,
                taps=None,
                fractional_bw=None,
        )
        self.freq_xlating_fir_filter_xxx_1_0 = filter.freq_xlating_fir_filter_fcc(1, (1, ), pscf1, samp_rate)
        self.freq_xlating_fir_filter_xxx_1 = filter.freq_xlating_fir_filter_ccc(1, (1, ), pscf1, samp_rate)
        self.freq_xlating_fir_filter_xxx_0 = filter.freq_xlating_fir_filter_ccc(5, (xlate_filter), xlatecenter, variable_sample_rate_0)
        self.blocks_multiply_const_vxx_0_0 = blocks.multiply_const_vff((amp_1, ))
        self.blocks_multiply_const_vxx_0 = blocks.multiply_const_vff((amp_1, ))
        self.blocks_complex_to_float_1 = blocks.complex_to_float(1)
        self.blocks_complex_to_float_0 = blocks.complex_to_float(1)
        self.band_pass_filter_0_0_0_0 = filter.fir_filter_ccf(4, firdes.band_pass(
        	1, bpsr, bplow_1, bphi_1, bptrans, firdes.WIN_HAMMING, 6.76))
        self.audio_sink_1 = audio.sink(48000, "Radio:NFM1", True)
        self.analog_nbfm_rx_0_0 = analog.nbfm_rx(
        	audio_rate=50000,
        	quad_rate=int(variable_sample_rate_0/5),
        	tau=75e-6,
        	max_dev=12500,
        )
        self.RTL820T = osmosdr.source( args="numchan=" + str(1) + " " + "" )
        self.RTL820T.set_sample_rate(variable_sample_rate_0)
        self.RTL820T.set_center_freq(CF, 0)
        self.RTL820T.set_freq_corr(0, 0)
        self.RTL820T.set_dc_offset_mode(2, 0)
        self.RTL820T.set_iq_balance_mode(0, 0)
        self.RTL820T.set_gain_mode(False, 0)
        self.RTL820T.set_gain(RF_Gain, 0)
        self.RTL820T.set_if_gain(20, 0)
        self.RTL820T.set_bb_gain(20, 0)
        self.RTL820T.set_antenna("", 0)
        self.RTL820T.set_bandwidth(1e6, 0)
          

        ##################################################
        # Connections
        ##################################################
        self.connect((self.RTL820T, 0), (self.freq_xlating_fir_filter_xxx_0, 0))    
        self.connect((self.analog_nbfm_rx_0_0, 0), (self.rational_resampler_xxx_1_0, 0))    
        self.connect((self.band_pass_filter_0_0_0_0, 0), (self.rational_resampler_xxx_1_0_0, 0))    
        self.connect((self.blocks_complex_to_float_0, 0), (self.blocks_multiply_const_vxx_0, 0))    
        self.connect((self.blocks_complex_to_float_1, 0), (self.blocks_multiply_const_vxx_0_0, 0))    
        self.connect((self.blocks_multiply_const_vxx_0, 0), (self.audio_sink_1, 0))    
        self.connect((self.blocks_multiply_const_vxx_0_0, 0), (self.audio_sink_1, 1))    
        self.connect((self.freq_xlating_fir_filter_xxx_0, 0), (self.analog_nbfm_rx_0_0, 0))    
        self.connect((self.freq_xlating_fir_filter_xxx_0, 0), (self.band_pass_filter_0_0_0_0, 0))    
        self.connect((self.freq_xlating_fir_filter_xxx_1, 0), (self.blocks_complex_to_float_1, 0))    
        self.connect((self.freq_xlating_fir_filter_xxx_1_0, 0), (self.blocks_complex_to_float_0, 0))    
        self.connect((self.rational_resampler_xxx_1_0, 0), (self.freq_xlating_fir_filter_xxx_1_0, 0))    
        self.connect((self.rational_resampler_xxx_1_0_0, 0), (self.freq_xlating_fir_filter_xxx_1, 0))    

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "Exp1")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_variable_sample_rate_0(self):
        return self.variable_sample_rate_0

    def set_variable_sample_rate_0(self, variable_sample_rate_0):
        self.variable_sample_rate_0 = variable_sample_rate_0
        self.set_xlate_filter(firdes.low_pass(1, self.variable_sample_rate_0, 125000, 25000, firdes.WIN_HAMMING, 6.76))
        self.RTL820T.set_sample_rate(self.variable_sample_rate_0)

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.set_xlate_filter2(firdes.low_pass(1, self.samp_rate, 4000, 1000, firdes.WIN_HAMMING, 6.76))

    def get_xlatecenter_4(self):
        return self.xlatecenter_4

    def set_xlatecenter_4(self, xlatecenter_4):
        self.xlatecenter_4 = xlatecenter_4

    def get_xlatecenter_3(self):
        return self.xlatecenter_3

    def set_xlatecenter_3(self, xlatecenter_3):
        self.xlatecenter_3 = xlatecenter_3

    def get_xlatecenter_2(self):
        return self.xlatecenter_2

    def set_xlatecenter_2(self, xlatecenter_2):
        self.xlatecenter_2 = xlatecenter_2

    def get_xlatecenter(self):
        return self.xlatecenter

    def set_xlatecenter(self, xlatecenter):
        self.xlatecenter = xlatecenter
        self.freq_xlating_fir_filter_xxx_0.set_center_freq(self.xlatecenter)

    def get_xlate_filter2(self):
        return self.xlate_filter2

    def set_xlate_filter2(self, xlate_filter2):
        self.xlate_filter2 = xlate_filter2

    def get_xlate_filter(self):
        return self.xlate_filter

    def set_xlate_filter(self, xlate_filter):
        self.xlate_filter = xlate_filter
        self.freq_xlating_fir_filter_xxx_0.set_taps((self.xlate_filter))

    def get_variable_1(self):
        return self.variable_1

    def set_variable_1(self, variable_1):
        self.variable_1 = variable_1

    def get_transition(self):
        return self.transition

    def set_transition(self, transition):
        self.transition = transition

    def get_rri(self):
        return self.rri

    def set_rri(self, rri):
        self.rri = rri

    def get_rrd(self):
        return self.rrd

    def set_rrd(self, rrd):
        self.rrd = rrd

    def get_quadrature(self):
        return self.quadrature

    def set_quadrature(self, quadrature):
        self.quadrature = quadrature

    def get_pscf4(self):
        return self.pscf4

    def set_pscf4(self, pscf4):
        self.pscf4 = pscf4

    def get_pscf3(self):
        return self.pscf3

    def set_pscf3(self, pscf3):
        self.pscf3 = pscf3

    def get_pscf2(self):
        return self.pscf2

    def set_pscf2(self, pscf2):
        self.pscf2 = pscf2

    def get_pscf1(self):
        return self.pscf1

    def set_pscf1(self, pscf1):
        self.pscf1 = pscf1
        self.freq_xlating_fir_filter_xxx_1.set_center_freq(self.pscf1)
        self.freq_xlating_fir_filter_xxx_1_0.set_center_freq(self.pscf1)

    def get_cutoff(self):
        return self.cutoff

    def set_cutoff(self, cutoff):
        self.cutoff = cutoff

    def get_bptrans(self):
        return self.bptrans

    def set_bptrans(self, bptrans):
        self.bptrans = bptrans
        self.band_pass_filter_0_0_0_0.set_taps(firdes.band_pass(1, self.bpsr, self.bplow_1, self.bphi_1, self.bptrans, firdes.WIN_HAMMING, 6.76))

    def get_bpsr(self):
        return self.bpsr

    def set_bpsr(self, bpsr):
        self.bpsr = bpsr
        self.band_pass_filter_0_0_0_0.set_taps(firdes.band_pass(1, self.bpsr, self.bplow_1, self.bphi_1, self.bptrans, firdes.WIN_HAMMING, 6.76))

    def get_bplow_4(self):
        return self.bplow_4

    def set_bplow_4(self, bplow_4):
        self.bplow_4 = bplow_4

    def get_bplow_3(self):
        return self.bplow_3

    def set_bplow_3(self, bplow_3):
        self.bplow_3 = bplow_3

    def get_bplow_2(self):
        return self.bplow_2

    def set_bplow_2(self, bplow_2):
        self.bplow_2 = bplow_2

    def get_bplow_1(self):
        return self.bplow_1

    def set_bplow_1(self, bplow_1):
        self.bplow_1 = bplow_1
        self.band_pass_filter_0_0_0_0.set_taps(firdes.band_pass(1, self.bpsr, self.bplow_1, self.bphi_1, self.bptrans, firdes.WIN_HAMMING, 6.76))

    def get_bphi_4(self):
        return self.bphi_4

    def set_bphi_4(self, bphi_4):
        self.bphi_4 = bphi_4

    def get_bphi_3(self):
        return self.bphi_3

    def set_bphi_3(self, bphi_3):
        self.bphi_3 = bphi_3

    def get_bphi_2(self):
        return self.bphi_2

    def set_bphi_2(self, bphi_2):
        self.bphi_2 = bphi_2

    def get_bphi_1(self):
        return self.bphi_1

    def set_bphi_1(self, bphi_1):
        self.bphi_1 = bphi_1
        self.band_pass_filter_0_0_0_0.set_taps(firdes.band_pass(1, self.bpsr, self.bplow_1, self.bphi_1, self.bptrans, firdes.WIN_HAMMING, 6.76))

    def get_audio_interp(self):
        return self.audio_interp

    def set_audio_interp(self, audio_interp):
        self.audio_interp = audio_interp

    def get_amp_4(self):
        return self.amp_4

    def set_amp_4(self, amp_4):
        self.amp_4 = amp_4

    def get_amp_3(self):
        return self.amp_3

    def set_amp_3(self, amp_3):
        self.amp_3 = amp_3

    def get_amp_2(self):
        return self.amp_2

    def set_amp_2(self, amp_2):
        self.amp_2 = amp_2

    def get_amp_1(self):
        return self.amp_1

    def set_amp_1(self, amp_1):
        self.amp_1 = amp_1
        self.blocks_multiply_const_vxx_0.set_k((self.amp_1, ))
        self.blocks_multiply_const_vxx_0_0.set_k((self.amp_1, ))

    def get_RF_Gain(self):
        return self.RF_Gain

    def set_RF_Gain(self, RF_Gain):
        self.RF_Gain = RF_Gain
        self.RTL820T.set_gain(self.RF_Gain, 0)

    def get_CF(self):
        return self.CF

    def set_CF(self, CF):
        self.CF = CF
        self.RTL820T.set_center_freq(self.CF, 0)


if __name__ == '__main__':
    parser = OptionParser(option_class=eng_option, usage="%prog: [options]")
    (options, args) = parser.parse_args()
    from distutils.version import StrictVersion
    if StrictVersion(Qt.qVersion()) >= StrictVersion("4.5.0"):
        Qt.QApplication.setGraphicsSystem(gr.prefs().get_string('qtgui','style','raster'))
    qapp = Qt.QApplication(sys.argv)
    tb = Exp1()
    tb.start()
    tb.show()

    def quitting():
        tb.stop()
        tb.wait()
    qapp.connect(qapp, Qt.SIGNAL("aboutToQuit()"), quitting)
    qapp.exec_()
    tb = None  # to clean up Qt widgets
