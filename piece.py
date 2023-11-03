import playfunction


piece = [
    #bar 1
    ['G4','qtr'],
    ['G4','qtr'],
    ['G4','qtr'],
    ['D#4','eighth.'],
    ['A#4','sixteenth'],
    #bar 2
    ['G4','qtr'],
    ['D#4','eighth.'],
    ['A#4','sixteenth'],
    ['G4','half'],
    #bar3
    ['D5','qtr'],
    ['D5','qtr'],
    ['D5','qtr'],
    ['D#5','eighth.'],
    ['A#4','sixteenth'],
    #bar4
    ['F#4','qtr'],
    ['D4','eighth.'],
    ['A#4','sixteenth'],
    ['G4','half'],
    #bar5
    ['G5','qtr'],
    ['G4','eighth.'],
    ['G4','sixteenth'],
    ['G5','qtr'],
    ['F#4','eighth'],
    ['E4','eighth'],
    #bar 6
    ['E5','qtr'],
    ['F#4','qtr'],
    ['C#5','qtr'],
    ['C5','eighth.'],
    ['B4','sixteenth'],
    #bar7
    ['B4','qtr'],
    ['D#4','qtr'],
    ['F#4','qtr'],
    ['D#4','eighth.'],
    ['F#4','sixteenth'],
    #bar8
    ['A#4','qtr'],
    ['G#4','eighth.'],
    ['B4','sixteenth'],
    ['D5','half']

]

playfunction.playSong(piece,60)



