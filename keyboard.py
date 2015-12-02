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
NOTEON = MIDION = 144
NOTEOFF = MIDIOFF = 128
CTRL = 176
PITCH = 224
# modulation is ctrl-176, 1

class RadioShiftSetter:
    def __init__(self,tb):
        self.tb = tb

    def set_freq(self, i, freq):
        print "set_freq %s %s" % (i,freq)
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
        return False
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
        return False
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
        def callback(message,ts):
            self.handle_message(message)
        self.device.set_callback(callback)
        
    def new_note(self, note_code):
        try:
            for i in range(0,len(self.freqs)):
                self.freqs[i] = False
            for note in self.notes:
                self.freqs[note[1]] = True
            i = self.freqs.index(False)
            self.freqs[i] = True
            print self.freqs
            print self.notes
            return (note_code, i)
        except ValueError:
            print self
            print self.freqs
        
    def shift_notes(self):
        if len(self.notes) >= self.max:
            note = self.notes[0]
            self.notes = self.notes[1:]
            self.send_off(note)
        
    def noteon(self, note_code):
        self.shift_notes()
        note = self.new_note(note_code)
        self.notes.append(note)
        self.send_on(note)

    def find_note(self,note_code):
        for x in self.notes:
            if x[0] == note_code:
                return x
        return None

    def remove_note(self, note_code):
        note = self.find_note(note_code)
        if not note is None:
            self.notes.remove(note)
        else:
            print "Note %s not found" % note_code
    
    def noteoff(self,note_code):
        note = self.find_note( note_code )
        if not note:
            print "Warning %s not found!" % note_code
            return
        self.send_off( note )
        self.notes.remove( note )

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

    def handle_message(self, msg):
        print msg                    
        # process message
        if msg[TYPE] == NOTEON:
            self.noteon(msg[INSTR])
        elif msg[TYPE] == NOTEOFF:
            self.noteoff(msg[INSTR])
        
    def run(self):
        raise "Not working"

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
    #collector.start()
    tb.Start(True)
    tb.Wait()
    collector.quit()
