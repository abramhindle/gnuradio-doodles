#!/usr/bin/env python2
##################################################
# GNU Radio Python Flow Graph
# Title: FM radio FFT example
# Author: David Haworth
# Generated: Sat Nov 28 18:16:28 2015
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

from gnuradio import analog
from gnuradio import audio
from gnuradio import eng_notation
from gnuradio import filter
from gnuradio import gr
from gnuradio import wxgui
from gnuradio.eng_option import eng_option
from gnuradio.fft import window
from gnuradio.filter import firdes
from gnuradio.wxgui import constsink_gl
from gnuradio.wxgui import fftsink2
from gnuradio.wxgui import forms
from gnuradio.wxgui import scopesink2
from gnuradio.wxgui import waterfallsink2
from grc_gnuradio import wxgui as grc_wxgui
from optparse import OptionParser
import osmosdr
import time
import wx


class top_block(grc_wxgui.top_block_gui):

    def __init__(self):
        grc_wxgui.top_block_gui.__init__(self, title="FM radio FFT example")
        _icon_path = "/usr/share/icons/hicolor/32x32/apps/gnuradio-grc.png"
        self.SetIcon(wx.Icon(_icon_path, wx.BITMAP_TYPE_ANY))

        ##################################################
        # Variables
        ##################################################
        self.variable_sample_rate_0 = variable_sample_rate_0 = 1.000E6
        self.xlatecenter = xlatecenter = 0
        self.xlate_filter = xlate_filter = firdes.low_pass(1, variable_sample_rate_0, 125000, 25000, firdes.WIN_HAMMING, 6.76)
        self.variable_static_text_0 = variable_static_text_0 = 'RTL R820T'
        self.variable_1 = variable_1 = 0
        self.transition = transition = 1e6
        self.samp_rate = samp_rate = 48000
        self.quadrature = quadrature = 500000
        self.cutoff = cutoff = 1e5
        self.audio_interp = audio_interp = 4
        self.RF_Gain = RF_Gain = 13
        self.CF = CF = 88.5e6

        ##################################################
        # Blocks
        ##################################################
        _xlatecenter_sizer = wx.BoxSizer(wx.VERTICAL)
        self._xlatecenter_text_box = forms.text_box(
        	parent=self.GetWin(),
        	sizer=_xlatecenter_sizer,
        	value=self.xlatecenter,
        	callback=self.set_xlatecenter,
        	label="center2",
        	converter=forms.float_converter(),
        	proportion=0,
        )
        self._xlatecenter_slider = forms.slider(
        	parent=self.GetWin(),
        	sizer=_xlatecenter_sizer,
        	value=self.xlatecenter,
        	callback=self.set_xlatecenter,
        	minimum=-1e6,
        	maximum=1e6,
        	num_steps=1000,
        	style=wx.SL_HORIZONTAL,
        	cast=float,
        	proportion=1,
        )
        self.GridAdd(_xlatecenter_sizer, 8, 0, 1, 5)
        self._variable_sample_rate_0_text_box = forms.text_box(
        	parent=self.GetWin(),
        	value=self.variable_sample_rate_0,
        	callback=self.set_variable_sample_rate_0,
        	label="Sample Rate: 1.024M, 1.4M, 1.8M, 1.92M, 2.048M, 2.4M & 2. 56M",
        	converter=forms.float_converter(),
        )
        self.GridAdd(self._variable_sample_rate_0_text_box, 7, 0, 1, 5)
        self.notebook_0 = self.notebook_0 = wx.Notebook(self.GetWin(), style=wx.NB_TOP)
        self.notebook_0.AddPage(grc_wxgui.Panel(self.notebook_0), "Spectrum")
        self.notebook_0.AddPage(grc_wxgui.Panel(self.notebook_0), "Waterfall")
        self.notebook_0.AddPage(grc_wxgui.Panel(self.notebook_0), "Constellation")
        self.notebook_0.AddPage(grc_wxgui.Panel(self.notebook_0), "Scope")
        self.GridAdd(self.notebook_0, 1, 0, 4, 5)
        _RF_Gain_sizer = wx.BoxSizer(wx.VERTICAL)
        self._RF_Gain_text_box = forms.text_box(
        	parent=self.GetWin(),
        	sizer=_RF_Gain_sizer,
        	value=self.RF_Gain,
        	callback=self.set_RF_Gain,
        	label="RF Gain",
        	converter=forms.float_converter(),
        	proportion=0,
        )
        self._RF_Gain_slider = forms.slider(
        	parent=self.GetWin(),
        	sizer=_RF_Gain_sizer,
        	value=self.RF_Gain,
        	callback=self.set_RF_Gain,
        	minimum=0,
        	maximum=45,
        	num_steps=45,
        	style=wx.SL_HORIZONTAL,
        	cast=float,
        	proportion=1,
        )
        self.GridAdd(_RF_Gain_sizer, 6, 0, 1, 5)
        _CF_sizer = wx.BoxSizer(wx.VERTICAL)
        self._CF_text_box = forms.text_box(
        	parent=self.GetWin(),
        	sizer=_CF_sizer,
        	value=self.CF,
        	callback=self.set_CF,
        	label="Center Frequency",
        	converter=forms.float_converter(),
        	proportion=0,
        )
        self._CF_slider = forms.slider(
        	parent=self.GetWin(),
        	sizer=_CF_sizer,
        	value=self.CF,
        	callback=self.set_CF,
        	minimum=87.9e6,
        	maximum=90e6,
        	num_steps=1000,
        	style=wx.SL_HORIZONTAL,
        	cast=float,
        	proportion=1,
        )
        self.GridAdd(_CF_sizer, 5, 0, 1, 5)
        self.wxgui_waterfallsink2_0 = waterfallsink2.waterfall_sink_c(
        	self.notebook_0.GetPage(1).GetWin(),
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
        	size=(575, 600),
        )
        self.notebook_0.GetPage(1).Add(self.wxgui_waterfallsink2_0.win)
        self.wxgui_scopesink2_0 = scopesink2.scope_sink_c(
        	self.notebook_0.GetPage(3).GetWin(),
        	title="Scope Plot",
        	sample_rate=variable_sample_rate_0,
        	v_scale=0,
        	v_offset=0,
        	t_scale=0,
        	ac_couple=False,
        	xy_mode=False,
        	num_inputs=1,
        	trig_mode=wxgui.TRIG_MODE_AUTO,
        	y_axis_label="Counts",
        )
        self.notebook_0.GetPage(3).Add(self.wxgui_scopesink2_0.win)
        self.wxgui_fftsink2_0 = fftsink2.fft_sink_c(
        	self.notebook_0.GetPage(0).GetWin(),
        	baseband_freq=CF,
        	y_per_div=10,
        	y_divs=10,
        	ref_level=0,
        	ref_scale=2.0,
        	sample_rate=variable_sample_rate_0,
        	fft_size=1024,
        	fft_rate=15,
        	average=False,
        	avg_alpha=None,
        	title="FFT Plot",
        	peak_hold=False,
        	size=(575, 600),
        )
        self.notebook_0.GetPage(0).Add(self.wxgui_fftsink2_0.win)
        self.wxgui_constellationsink2_0 = constsink_gl.const_sink_c(
        	self.notebook_0.GetPage(2).GetWin(),
        	title="Constellation Plot",
        	sample_rate=variable_sample_rate_0,
        	frame_rate=5,
        	const_size=2048,
        	M=4,
        	theta=0,
        	loop_bw=6.28/100.0,
        	fmax=0.06,
        	mu=0.5,
        	gain_mu=0.005,
        	symbol_rate=variable_sample_rate_0/4.,
        	omega_limit=0.005,
        	size=(575, 600),
        )
        self.notebook_0.GetPage(2).Add(self.wxgui_constellationsink2_0.win)
        self._variable_static_text_0_static_text = forms.static_text(
        	parent=self.GetWin(),
        	value=self.variable_static_text_0,
        	callback=self.set_variable_static_text_0,
        	label="SDR ",
        	converter=forms.str_converter(),
        )
        self.GridAdd(self._variable_static_text_0_static_text, 0, 0, 1, 5)
        self.rational_resampler_xxx_1_0 = filter.rational_resampler_fff(
                interpolation=48,
                decimation=50,
                taps=None,
                fractional_bw=None,
        )
        self.rational_resampler_xxx_1 = filter.rational_resampler_fff(
                interpolation=48,
                decimation=50,
                taps=None,
                fractional_bw=None,
        )
        self.rational_resampler_xxx_0 = filter.rational_resampler_ccc(
                interpolation=samp_rate * audio_interp,
                decimation=int(variable_sample_rate_0),
                taps=None,
                fractional_bw=None,
        )
        self.low_pass_filter_0 = filter.fir_filter_ccf(5, firdes.low_pass(
        	1, variable_sample_rate_0, 5000, 8000, firdes.WIN_HAMMING, 6.76))
        self.freq_xlating_fir_filter_xxx_0 = filter.freq_xlating_fir_filter_ccc(5, (xlate_filter), xlatecenter, variable_sample_rate_0)
        self.audio_sink_1_0 = audio.sink(48000, "Radio:NFM-Center", True)
        self.audio_sink_1 = audio.sink(48000, "Radio:NFM", True)
        self.audio_sink_0 = audio.sink(48000, "Radio:WFM", False)
        self.analog_wfm_rcv_0 = analog.wfm_rcv(
        	quad_rate=samp_rate * audio_interp,
        	audio_decimation=audio_interp,
        )
        self.analog_nbfm_rx_0_0 = analog.nbfm_rx(
        	audio_rate=50000,
        	quad_rate=int(variable_sample_rate_0/5),
        	tau=75e-6,
        	max_dev=12500,
        )
        self.analog_nbfm_rx_0 = analog.nbfm_rx(
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
        self.connect((self.RTL820T, 0), (self.low_pass_filter_0, 0))    
        self.connect((self.RTL820T, 0), (self.rational_resampler_xxx_0, 0))    
        self.connect((self.RTL820T, 0), (self.wxgui_constellationsink2_0, 0))    
        self.connect((self.RTL820T, 0), (self.wxgui_fftsink2_0, 0))    
        self.connect((self.RTL820T, 0), (self.wxgui_scopesink2_0, 0))    
        self.connect((self.RTL820T, 0), (self.wxgui_waterfallsink2_0, 0))    
        self.connect((self.analog_nbfm_rx_0, 0), (self.rational_resampler_xxx_1, 0))    
        self.connect((self.analog_nbfm_rx_0_0, 0), (self.rational_resampler_xxx_1_0, 0))    
        self.connect((self.analog_wfm_rcv_0, 0), (self.audio_sink_0, 0))    
        self.connect((self.freq_xlating_fir_filter_xxx_0, 0), (self.analog_nbfm_rx_0_0, 0))    
        self.connect((self.low_pass_filter_0, 0), (self.analog_nbfm_rx_0, 0))    
        self.connect((self.rational_resampler_xxx_0, 0), (self.analog_wfm_rcv_0, 0))    
        self.connect((self.rational_resampler_xxx_1, 0), (self.audio_sink_1, 0))    
        self.connect((self.rational_resampler_xxx_1_0, 0), (self.audio_sink_1_0, 0))    


    def get_variable_sample_rate_0(self):
        return self.variable_sample_rate_0

    def set_variable_sample_rate_0(self, variable_sample_rate_0):
        self.variable_sample_rate_0 = variable_sample_rate_0
        self._variable_sample_rate_0_text_box.set_value(self.variable_sample_rate_0)
        self.set_xlate_filter(firdes.low_pass(1, self.variable_sample_rate_0, 125000, 25000, firdes.WIN_HAMMING, 6.76))
        self.RTL820T.set_sample_rate(self.variable_sample_rate_0)
        self.low_pass_filter_0.set_taps(firdes.low_pass(1, self.variable_sample_rate_0, 5000, 8000, firdes.WIN_HAMMING, 6.76))
        self.wxgui_constellationsink2_0.set_sample_rate(self.variable_sample_rate_0)
        self.wxgui_fftsink2_0.set_sample_rate(self.variable_sample_rate_0)
        self.wxgui_scopesink2_0.set_sample_rate(self.variable_sample_rate_0)
        self.wxgui_waterfallsink2_0.set_sample_rate(self.variable_sample_rate_0)

    def get_xlatecenter(self):
        return self.xlatecenter

    def set_xlatecenter(self, xlatecenter):
        self.xlatecenter = xlatecenter
        self._xlatecenter_slider.set_value(self.xlatecenter)
        self._xlatecenter_text_box.set_value(self.xlatecenter)
        self.freq_xlating_fir_filter_xxx_0.set_center_freq(self.xlatecenter)

    def get_xlate_filter(self):
        return self.xlate_filter

    def set_xlate_filter(self, xlate_filter):
        self.xlate_filter = xlate_filter
        self.freq_xlating_fir_filter_xxx_0.set_taps((self.xlate_filter))

    def get_variable_static_text_0(self):
        return self.variable_static_text_0

    def set_variable_static_text_0(self, variable_static_text_0):
        self.variable_static_text_0 = variable_static_text_0
        self._variable_static_text_0_static_text.set_value(self.variable_static_text_0)

    def get_variable_1(self):
        return self.variable_1

    def set_variable_1(self, variable_1):
        self.variable_1 = variable_1

    def get_transition(self):
        return self.transition

    def set_transition(self, transition):
        self.transition = transition

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate

    def get_quadrature(self):
        return self.quadrature

    def set_quadrature(self, quadrature):
        self.quadrature = quadrature

    def get_cutoff(self):
        return self.cutoff

    def set_cutoff(self, cutoff):
        self.cutoff = cutoff

    def get_audio_interp(self):
        return self.audio_interp

    def set_audio_interp(self, audio_interp):
        self.audio_interp = audio_interp

    def get_RF_Gain(self):
        return self.RF_Gain

    def set_RF_Gain(self, RF_Gain):
        self.RF_Gain = RF_Gain
        self._RF_Gain_slider.set_value(self.RF_Gain)
        self._RF_Gain_text_box.set_value(self.RF_Gain)
        self.RTL820T.set_gain(self.RF_Gain, 0)

    def get_CF(self):
        return self.CF

    def set_CF(self, CF):
        self.CF = CF
        self._CF_slider.set_value(self.CF)
        self._CF_text_box.set_value(self.CF)
        self.RTL820T.set_center_freq(self.CF, 0)
        self.wxgui_fftsink2_0.set_baseband_freq(self.CF)
        self.wxgui_waterfallsink2_0.set_baseband_freq(self.CF)


if __name__ == '__main__':
    parser = OptionParser(option_class=eng_option, usage="%prog: [options]")
    (options, args) = parser.parse_args()
    tb = top_block()
    tb.Start(True)
    tb.Wait()
