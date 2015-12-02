import sys
import rtmidi
import threading

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
import RadioShifter

VELOCITY = 2
TYPE = 0
INSTR = 1
MIDION = 144
MIDIOFF = 128
CTRL = 176
PITCH = 224
# modulation is ctrl-176, 1

class RadioShiftSetter:
    def __init__(self,tb):
        self.tb = tb

    def set_freq(self, i, freq):
        tb = self.tb
	if i == 1:
	    tb.set_xlatecenter(freq)
	elif i == 2:
	    tb.set_xlatecenter_2(freq)
	elif i == 3:
	    tb.set_xlatecenter_3(freq)
	elif i == 4:
	    tb.set_xlatecenter_4(freq)
    def set_on(self, i):
        tb = self.tb
	if i == 1:
	    tb.set_amp_1(1.0)
	elif i == 2:
	    tb.set_amp_2(1.0)
	elif i == 3:
	    tb.set_amp_3(1.0)
	elif i == 4:
	    tb.set_amp_4(1.0)
    def set_off(self, i):
        tb = self.tb
	if i == 1:
	    tb.set_amp_1(0.0)
	elif i == 2:
	    tb.set_amp_2(0.0)
	elif i == 3:
	    tb.set_amp_3(0.0)
	elif i == 4:
	    tb.set_amp_4(0.0)

            


class Collector(threading.Thread):
    def __init__(self, device, port, setter = None, minnote=36, maxnote=84,bw=1e6):
        threading.Thread.__init__(self)
        self.setDaemon(True)
        self.port = port
        self.portName = device.get_port_name(port)
        self.device = device
        self.quit = False
        self.notes = list()
        self.max = 4
        self.minnote = minnote
        self.maxnote = maxnote
        self.freqs = self.max * [False]
        self.setter = setter
        self.bw = bw
        
    def new_note(self, note_code):
        i = self.freqs.index(False)
        self.freqs[i] = True
        return (note_code, i)
        
    def shift_notes(self):
        if len(self.notes) >= self.max - 1:
            note = self.notes[0]
            self.notes = self.notes[1:]
            self.send_off(note)
        
    def noteon(self, note_code):
        self.shift_notes()
        note = self.new_note(note_code)
        self.notes.append(note)
        self.send_on(note)

    def noteoff(self,note_code):
        if note in self.notes:
            self.notes.remove(note)
        self.send_off(note)

    def send_on(self,note):        
        (note_code, i) = note        
        if self.setter:
            r = self.maxnote - self.minnote            
            freq = self.bw * (((note_code - self.minnote)/float(r)) - 0.5)
            self.setter.set_freq(i, freq)
            self.setter.set_on(i)
            
    def send_off(self,note):
        (note_code, i) = note        
        self.setter.set_off(i)
        
    def run(self):
        #self.device.ignore_types(True, False, True)
        while True:
            if self.quit:
                return
            msg = self.device.get_message()
            if msg:
                print msg
                # process message

if __name__ == '__main__':
    parser = OptionParser(option_class=eng_option, usage="%prog: [options]")
    (options, args) = parser.parse_args()
    tb = RadioShifter.RadioShifter()
    midiin = rtmidi.MidiIn()
    available_ports = midiin.get_ports()
    devname = u'BEHRINGER UMC404 28:0'
    devname = u'masterkey 49 32:0'
    devindex = available_ports.index(devname)
    minnote = 36
    maxnote = 84
    device = midiin.open_port(devindex)
    setter = RadioShiftSetter(tb)    
    collector = Collector(device, devindex, setter=setter)
    collector.start()
    tb.Start(True)
    tb.Wait()
    collector.quit()
