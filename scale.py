import playfunction

playfunction.settings.function = 'sin'

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

playfunction.playSong(scaletravel,120)
playfunction.playSong(scaletravel[::-1],120)


