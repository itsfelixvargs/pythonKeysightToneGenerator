from functionDictionary import funcDict
import pyvisa as pyv
from time import sleep
import settings
from notedictionary import scale

resMan = pyv.ResourceManager()
#wvfdevice = "__UNLOADED__"

''' MOVE TO MAIN'''
global wvfdevice

def IdentifyDevice():
    global wvfdevice
    DevID = settings.DevID
    print("DevID is:")
    print(DevID)
    timeout = 1000
    wvfdevice = resMan.open_resource(DevID)
    print("\nWaveform Generator "+ DevID +" is connected")
    resMan.list_resources_info(DevID)


def write(cmd):
    try:
        global wvfdevice
        wvfdevice.write(cmd)
        print("\nEXECUTED: " + cmd)
    except:
        print("\nERR: Cannot send for some reason | " + cmd)



def playnote(   note,  noteDuration,   funct = settings.default_function,   pieceSpeed = 30,  amp = settings.magnitude,   offset = settings.offset    ):
    
    #   Note durations
    durationDict = {
        'full'      :   1,
        'half'      :   0.5,
        'half.'     :   0.75,
        'qtr'       :   0.25,
        'qtr.'      :   0.375,
        'eighth'    :   0.125,
        'eighth.'   :   0.1875,
        'sixteenth' :   0.0625
    }
    duration = durationDict.get(noteDuration) / ( pieceSpeed / 60)
    freq = scale.get(note)

    #   print the output SCPI command

    write("SOUR1:APPL:{}{} HZ, {}, {}".format(funcDict.get(funct),freq, amp, offset))

    
    write("OUTP2 ON")
    write("OUTP1 ON")
    # note duration

    sleep(duration)




def playSong(song,tempo):
    global songtempo
    songtempo = tempo
    for i in song:
        playnote(*i)
    #ENDING
    write("OUTP2 OFF")
    write("OUTP1 OFF")



    
if __name__ == "playfunction":
    IdentifyDevice()
    write("SOUR2:TRAC ON")
    write("OUTP1:LOAD 33")
    write("OUTP2:LOAD 33")


if __name__ == "__main__":
    IdentifyDevice()
    write("SOUR2:TRAC ON")
    write("OUTP1:LOAD 33")
    write("OUTP2:LOAD 33")
    
    settings.default_function = 'sin'
    scaletravel = [
        ['C3','qtr'],
        ['C#3','qtr'],
        ['D3','qtr'],
        ['D#3','qtr'],
        ['E3','qtr'],
        ['F3','qtr'],
        ['F#3','qtr'],
        ['G3','qtr'],
        ['Ab3','qtr'],
        ['A3','qtr'],
        ['Bb3','qtr'],
        ['B3','qtr'],
        ['C4','qtr'],
        ['C#4','qtr'],
        ['D4','qtr'],
        ['Eb4','qtr'],
        ['E4','qtr'],
        ['F4','qtr'],
        ['F#4','qtr'],
        ['G4','qtr'],
        ['G#4','qtr'],
        ['Ab4','qtr'],
        ['A4','qtr'],
        ['A#4','qtr'],
        ['Bb4','qtr'],
        ['B4','qtr'],
        ['C5','qtr']
    ]

    playSong(scaletravel,120)
    playSong(scaletravel[::-1],120)

    
