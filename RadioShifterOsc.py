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
import RadioShifterHeadless
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
        print "set_amp %s" % i
	if i == 1:
	    tb.set_amp_1(f)
	elif i == 2:
	    tb.set_amp_2(f)
	elif i == 3:
	    tb.set_amp_3(f)
	elif i == 4:
	    tb.set_amp_4(f)
        return None
    
    @make_method(None, None)
    def fallback(self, path, args):
        print "received unknown message '%s'" % path

import time
if __name__ == '__main__':
    parser = OptionParser(option_class=eng_option, usage="%prog: [options]")
    (options, args) = parser.parse_args()
    tb = RadioShifterHeadless.RadioShifterHeadless()
    try:
        server = MyOscServer()
    except ServerError, err:
        print str(err)
        sys.exit()
    print "NOUTPUT %s" % tb.max_noutput_items()
    buffersize = 256
    items = 64
    tb.audio_sink_1_0_1.set_max_output_buffer(buffersize)
    tb.audio_sink_1_0_0_0.set_max_output_buffer(buffersize)
    tb.audio_sink_1_0_0.set_max_output_buffer(buffersize)
    tb.audio_sink_1_0.set_max_output_buffer(buffersize)
    tb.audio_sink_1_0_1.set_max_noutput_items(buffersize)
    tb.audio_sink_1_0_0_0.set_max_noutput_items(buffersize)
    tb.audio_sink_1_0_0.set_max_noutput_items(buffersize)
    tb.audio_sink_1_0.set_max_noutput_items(buffersize)

    
    # tb.Start(True)
    #tb.start()
    #tb.Start(True)
    #tb.Wait()
    #tb.start()
    #tb.start(512)
    tb.set_CF(125.6e6)
    tb.start(5)

    while True:
        #time.sleep(0.01)
        server.recv(10)

    
