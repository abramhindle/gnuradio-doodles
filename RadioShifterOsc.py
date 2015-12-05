if __name__ == '__main__':
    import ctypes
    import sys
    if sys.platform.startswith('linux'):
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print "Warning: failed to XInitThreads()"

from optparse import OptionParser
from gnuradio.eng_option import eng_option
import RadioShifterPitchShiftHeadless
from liblo import *
tb = None
class MyOscServer(Server):
    def __init__(self):
        Server.__init__(self, 1234)

    @make_method('/foo', 'ifs')
    def foo_callback(self, path, args):
        i, f, s = args
        print "received message '%s' with arguments: %d, %f, %s" % (path, i, f, s)

    @make_method('/center', 'if')
    def center_callback(self, path, args):
        i, f = args
        print "center received message '%s' with arguments: %d, %f" % (path, i, f)
        if not tb is None:
            if i == 1:
                tb.set_xlatecenter(f)
            elif i == 2:
                tb.set_xlatecenter_2(f)
            elif i == 3:
                tb.set_xlatecenter_3(f)
            elif i == 4:
                tb.set_xlatecenter_4(f)
            elif i == 0:
                tb.set_CF(f)
            else:
                print "Invalid index %s" % i
        return None

    @make_method('/low', 'if')
    def low_callback(self, path, args):
        i, f = args
        print "low received message '%s' with arguments: %d, %f" % (path, i, f)
        if not tb is None:
            if i == 1:
                tb.set_bplow_1(f)
            elif i == 2:
                tb.set_bplow_2(f)
            elif i == 3:
                tb.set_bplow_3(f)
            elif i == 4:
                tb.set_bplow_4(f)
            else:
                print "Invalid index %s" % i
        return None

    @make_method('/high', 'if')
    def high_callback(self, path, args):
        i, f = args
        print "high received message '%s' with arguments: %d, %f" % (path, i, f)
        if not tb is None:
            if i == 1:
                tb.set_bphi_1(f)
            elif i == 2:
                tb.set_bphi_2(f)
            elif i == 3:
                tb.set_bphi_3(f)
            elif i == 4:
                tb.set_bphi_4(f)
            else:
                print "Invalid index %s" % i
        return None
    
    @make_method('/amp', 'if')
    def amp_callback(self, path, args):
        i, f = args
        print "set_amp %s %s" % (i,f)
	if i == 1:
	    tb.set_amp_1(f)
	elif i == 2:
	    tb.set_amp_2(f)
	elif i == 3:
	    tb.set_amp_3(f)
	elif i == 4:
	    tb.set_amp_4(f)
        return None

    @make_method('/pscf', 'if')
    def pscf_callback(self, path, args):
        i, f = args
        print "set_pscf %s %s" % (i,f)
	if i == 1:
	    tb.set_pscf1(f)
	elif i == 2:
	    tb.set_pscf2(f)
	elif i == 3:
	    tb.set_pscf3(f)
	elif i == 4:
	    tb.set_pscf4(f)
        return None

    @make_method('/pscfshift', 'f')
    def pscfshift_callback(self, path, args):
        f = args[0]
        print "set_pscfshift %s" % (f)
	tb.set_pscfshift(f)
    @make_method('/globaltune', 'f')
    def globaltune_callback(self, path, args):
        f = args[0]
        print "set_globaltune %s" % (f)
	tb.set_globaltune(f)
        

    
    @make_method(None, None)
    def fallback(self, path, args):
        print "received unknown message '%s'" % path

import time
if __name__ == '__main__':
    parser = OptionParser(option_class=eng_option, usage="%prog: [options]")
    (options, args) = parser.parse_args()
    tb = RadioShifterPitchShiftHeadless.RadioShifterPitchShiftHeadless()
    try:
        server = MyOscServer()
    except ServerError, err:
        print str(err)
        sys.exit()
    buffersize = 1024
    items = 256
    tb.set_max_noutput_items(items)
    tb.audio_sink_1.set_max_output_buffer(buffersize)
    tb.audio_sink_2.set_max_output_buffer(buffersize)
    tb.audio_sink_3.set_max_output_buffer(buffersize)
    tb.audio_sink_4.set_max_output_buffer(buffersize)
    tb.audio_sink_1.set_max_noutput_items(items)
    tb.audio_sink_2.set_max_noutput_items(items)
    tb.audio_sink_3.set_max_noutput_items(items)
    tb.audio_sink_4.set_max_noutput_items(items)
    
    tb.set_CF(125.5e6)
    #tb.set_CF(88.5e6)
    tb.start(16)

    while True:
        server.recv(33)

    
