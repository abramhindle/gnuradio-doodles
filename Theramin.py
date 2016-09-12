#!/usr/bin/env python2
##################################################
# GNU Radio Python Flow Graph
# Title: FM radio FFT example
# Author: David Haworth, Abram Hindle
# Generated: Wed Jan 27 20:41:28 2016
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

from gnuradio import blocks
from gnuradio import eng_notation
from gnuradio import gr
from gnuradio import video_sdl
from gnuradio import wxgui
from gnuradio.eng_option import eng_option
from gnuradio.fft import window
from gnuradio.filter import firdes
from gnuradio.wxgui import waterfallsink2
from grc_gnuradio import wxgui as grc_wxgui
from optparse import OptionParser
import osmosdr
import threading
import time
import wx


class Theramin(grc_wxgui.top_block_gui):

    def __init__(self):
        grc_wxgui.top_block_gui.__init__(self, title="FM radio FFT example")
        _icon_path = "/usr/share/icons/hicolor/32x32/apps/gnuradio-grc.png"
        self.SetIcon(wx.Icon(_icon_path, wx.BITMAP_TYPE_ANY))

        ##################################################
        # Variables
        ##################################################
        self.variable_sample_rate_0 = variable_sample_rate_0 = 1e6
        self.samp_rate = samp_rate = 44100
        self.xlatecenter_8 = xlatecenter_8 = 0
        self.xlatecenter_7 = xlatecenter_7 = 0
        self.xlatecenter_6 = xlatecenter_6 = 0
        self.xlatecenter_5 = xlatecenter_5 = 0
        self.xlatecenter_4 = xlatecenter_4 = 0
        self.xlatecenter_3 = xlatecenter_3 = 0
        self.xlatecenter_2 = xlatecenter_2 = 0
        self.xlatecenter = xlatecenter = 0
        self.xlate_filter2 = xlate_filter2 = firdes.low_pass(1, samp_rate, 4000, 1000, firdes.WIN_HAMMING, 6.76)
        self.xlate_filter = xlate_filter = firdes.low_pass(1, variable_sample_rate_0, 125000, 25000, firdes.WIN_HAMMING, 6.76)
        self.variable_function_probe_0 = variable_function_probe_0 = 0
        self.variable_1 = variable_1 = 0
        self.transition = transition = 1e6
        self.rri = rri = 441
        self.rrd = rrd = 500
        self.quadrature = quadrature = 500000
        self.pscfshift = pscfshift = 0
        self.pscf8 = pscf8 = 0
        self.pscf7 = pscf7 = 0
        self.pscf6 = pscf6 = 0
        self.pscf5 = pscf5 = 0
        self.pscf4 = pscf4 = 0
        self.pscf3 = pscf3 = 0
        self.pscf2 = pscf2 = 0
        self.pscf1 = pscf1 = 0
        self.globaltune = globaltune = 0
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
        self.amp_fm = amp_fm = 1
        self.amp_am = amp_am = 1
        self.amp_8 = amp_8 = 0
        self.amp_7 = amp_7 = 0
        self.amp_6 = amp_6 = 0
        self.amp_5 = amp_5 = 0
        self.amp_4 = amp_4 = 0
        self.amp_3 = amp_3 = 0
        self.amp_2 = amp_2 = 0
        self.amp_1 = amp_1 = 0
        self.RF_Gain = RF_Gain = 35
        self.CF = CF = 125.6e6

        ##################################################
        # Blocks
        ##################################################
        self.wxgui_waterfallsink2_0 = waterfallsink2.waterfall_sink_c(
        	self.GetWin(),
        	baseband_freq=CF,
        	dynamic_range=100,
        	ref_level=0,
        	ref_scale=2.0,
        	sample_rate=variable_sample_rate_0,
        	fft_size=512,
        	fft_rate=15,
        	average=False,
        	avg_alpha=None,
        	title="Waterfall Plot",
        	size=(924,668),
        )
        self.Add(self.wxgui_waterfallsink2_0.win)
        self.video_sdl_sink_0 = video_sdl.sink_s(0, 640, 480, 0, 640, 480)
        def _variable_function_probe_0_probe():
            while True:
                val = self.my_block_0.get_number()
                try:
                    self.set_variable_function_probe_0(val)
                except AttributeError:
                    pass
                time.sleep(1.0 / (10))
        _variable_function_probe_0_thread = threading.Thread(target=_variable_function_probe_0_probe)
        _variable_function_probe_0_thread.daemon = True
        _variable_function_probe_0_thread.start()
        self.blocks_unpacked_to_packed_xx_0 = blocks.unpacked_to_packed_ss(2, gr.GR_MSB_FIRST)
        self.blocks_float_to_short_0_0 = blocks.float_to_short(1, 1)
        self.blocks_float_to_short_0 = blocks.float_to_short(1, 1)
        self.blocks_complex_to_float_0 = blocks.complex_to_float(1)
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
        self.connect((self.RTL820T, 0), (self.blocks_complex_to_float_0, 0))    
        self.connect((self.RTL820T, 0), (self.wxgui_waterfallsink2_0, 0))    
        self.connect((self.blocks_complex_to_float_0, 0), (self.blocks_float_to_short_0, 0))    
        self.connect((self.blocks_complex_to_float_0, 1), (self.blocks_float_to_short_0_0, 0))    
        self.connect((self.blocks_float_to_short_0, 0), (self.blocks_unpacked_to_packed_xx_0, 0))    
        self.connect((self.blocks_float_to_short_0_0, 0), (self.video_sdl_sink_0, 1))    
        self.connect((self.blocks_unpacked_to_packed_xx_0, 0), (self.video_sdl_sink_0, 0))    


    def get_variable_sample_rate_0(self):
        return self.variable_sample_rate_0

    def set_variable_sample_rate_0(self, variable_sample_rate_0):
        self.variable_sample_rate_0 = variable_sample_rate_0
        self.set_xlate_filter(firdes.low_pass(1, self.variable_sample_rate_0, 125000, 25000, firdes.WIN_HAMMING, 6.76))
        self.RTL820T.set_sample_rate(self.variable_sample_rate_0)
        self.wxgui_waterfallsink2_0.set_sample_rate(self.variable_sample_rate_0)

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.set_xlate_filter2(firdes.low_pass(1, self.samp_rate, 4000, 1000, firdes.WIN_HAMMING, 6.76))

    def get_xlatecenter_8(self):
        return self.xlatecenter_8

    def set_xlatecenter_8(self, xlatecenter_8):
        self.xlatecenter_8 = xlatecenter_8

    def get_xlatecenter_7(self):
        return self.xlatecenter_7

    def set_xlatecenter_7(self, xlatecenter_7):
        self.xlatecenter_7 = xlatecenter_7

    def get_xlatecenter_6(self):
        return self.xlatecenter_6

    def set_xlatecenter_6(self, xlatecenter_6):
        self.xlatecenter_6 = xlatecenter_6

    def get_xlatecenter_5(self):
        return self.xlatecenter_5

    def set_xlatecenter_5(self, xlatecenter_5):
        self.xlatecenter_5 = xlatecenter_5

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

    def get_xlate_filter2(self):
        return self.xlate_filter2

    def set_xlate_filter2(self, xlate_filter2):
        self.xlate_filter2 = xlate_filter2

    def get_xlate_filter(self):
        return self.xlate_filter

    def set_xlate_filter(self, xlate_filter):
        self.xlate_filter = xlate_filter

    def get_variable_function_probe_0(self):
        return self.variable_function_probe_0

    def set_variable_function_probe_0(self, variable_function_probe_0):
        self.variable_function_probe_0 = variable_function_probe_0

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

    def get_pscfshift(self):
        return self.pscfshift

    def set_pscfshift(self, pscfshift):
        self.pscfshift = pscfshift

    def get_pscf8(self):
        return self.pscf8

    def set_pscf8(self, pscf8):
        self.pscf8 = pscf8

    def get_pscf7(self):
        return self.pscf7

    def set_pscf7(self, pscf7):
        self.pscf7 = pscf7

    def get_pscf6(self):
        return self.pscf6

    def set_pscf6(self, pscf6):
        self.pscf6 = pscf6

    def get_pscf5(self):
        return self.pscf5

    def set_pscf5(self, pscf5):
        self.pscf5 = pscf5

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

    def get_globaltune(self):
        return self.globaltune

    def set_globaltune(self, globaltune):
        self.globaltune = globaltune

    def get_cutoff(self):
        return self.cutoff

    def set_cutoff(self, cutoff):
        self.cutoff = cutoff

    def get_bptrans(self):
        return self.bptrans

    def set_bptrans(self, bptrans):
        self.bptrans = bptrans

    def get_bpsr(self):
        return self.bpsr

    def set_bpsr(self, bpsr):
        self.bpsr = bpsr

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

    def get_audio_interp(self):
        return self.audio_interp

    def set_audio_interp(self, audio_interp):
        self.audio_interp = audio_interp

    def get_amp_fm(self):
        return self.amp_fm

    def set_amp_fm(self, amp_fm):
        self.amp_fm = amp_fm

    def get_amp_am(self):
        return self.amp_am

    def set_amp_am(self, amp_am):
        self.amp_am = amp_am

    def get_amp_8(self):
        return self.amp_8

    def set_amp_8(self, amp_8):
        self.amp_8 = amp_8

    def get_amp_7(self):
        return self.amp_7

    def set_amp_7(self, amp_7):
        self.amp_7 = amp_7

    def get_amp_6(self):
        return self.amp_6

    def set_amp_6(self, amp_6):
        self.amp_6 = amp_6

    def get_amp_5(self):
        return self.amp_5

    def set_amp_5(self, amp_5):
        self.amp_5 = amp_5

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
        self.wxgui_waterfallsink2_0.set_baseband_freq(self.CF)


if __name__ == '__main__':
    parser = OptionParser(option_class=eng_option, usage="%prog: [options]")
    (options, args) = parser.parse_args()
    tb = Theramin()
    tb.Start(True)
    tb.Wait()
