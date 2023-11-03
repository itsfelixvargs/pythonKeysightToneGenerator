'''Generation of the scale from C3 to C5, and duration'''

'''OFFSET BY 3 to C which starts the scale'''

notes = ["A","A#/Bb","B","C","C#/Db","D","D#/Eb","E","F","F#/Gb","G","G#/Ab"]
a4frequency = 440.0
scale = {}
octmin = 3
octmax = 5
for i in range(octmin - 1 , octmax):
    for k in range(len(notes)):
        j = (k + 3) % 12   
        #For labelling the notes, we use the above as it loops from C to C. But for calculating the frequency we should not loop over.

        freq  =   round (   pow(2,   (  (k + 3) / 12    ) + (i - 4) )   *  a4frequency,    2)
        if(len(notes[j]) == 5):
            scale.update({notes[j][0:2]   + str(i + 1)  :   freq})
            scale.update({notes[j][3:]    + str(i + 1)  :   freq})
        else:
            scale.update({notes[j] + str(i + 1): freq})


if __name__ == "__main__":
    # print("notes:\n")
    # for i in scale:
    #     print("['{}','{}'],".format(i ,'qtr'))

    print(scale)
