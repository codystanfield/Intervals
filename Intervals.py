#!/usr/bin/env python3

'''
Program that calculates the interval between two notes
NOTE: does not handle bad input well
'''

import sys

naturals = {'C': 0, 'D': 1, 'E': 2, 'F': 3, 'G': 4, 'A': 5, 'B': 6}

chromatic_scale = {'Cbb': 11, 'Cb': 0, 'C': 1, 'C#': 2, 'C##': 3,
                   'Dbb': 1, 'Db': 2, 'D': 3, 'D#': 4, 'D##': 5,
                   'Ebb': 3, 'Eb': 4, 'E': 5, 'E#': 6, 'E##': 7,
                   'Fbb': 4, 'Fb': 5, 'F': 6, 'F#': 7, 'F##': 8,
                   'Gbb': 6, 'Gb': 7, 'G': 8, 'G#': 9, 'G##': 10,
                   'Abb': 8, 'Ab': 9, 'A': 10, 'A#': 11, 'A##': 12,
                   'Bbb': 10, 'Bb': 11, 'B': 0, 'B#': 1, 'B##': 2}

# TODO: unisons
intervals = {(2, 0): 'd2', (2, 1): 'm2', (2, 2): 'M2', (2, 3): 'A2',
             (3, 2): 'd3', (3, 3): 'm3', (3, 4): 'M3', (3, 5): 'A3',
             (4, 4): 'd4', (4, 5): 'P4', (4, 6): 'A4',
             (5, 6): 'd5', (5, 7): 'P5', (5, 8): 'A5',
             (6, 7): 'd6', (6, 8): 'm6', (6, 9): 'M6', (6, 10): 'A6',
             (7, 9): 'd7', (7, 10): 'm7', (7, 11): 'M7', (7, 12): 'A7',
             (8, 11): 'd8', (8, 12): 'P8', (8, 13): 'A8'}


def main():
    while True:
        try:
            note1 = input('Enter the lower note: ')
            note2 = input('Enter the higher note: ')
            
            note1 = normalize_note(note1)
            note2 = normalize_note(note2)
            
            distance = get_distance(note1, note2)
            num_half_steps = get_num_half_steps(note1, note2)
            
            print('Interval: {0}'.format(get_interval(distance, num_half_steps)))
        except (KeyboardInterrupt, EOFError):
            print()
            sys.exit()
            

def normalize_note(note):
    if len(note) == 1:
        return note.upper()
    return '{0}{1}'.format(note[0].upper(), note[1:])


def get_distance(note1, note2):
    val1 = naturals[note2[0]]
    val2 = naturals[note1[0]]
    
    if val1 < val2:
        return val1 + 8 - val2
    return val1 - val2 + 1
        
        
def get_num_half_steps(note1, note2):
    val1 = chromatic_scale[note2]
    val2 = chromatic_scale[note1]
    
    if val1 < val2:
        val1 += 12
    return val1 - val2


def get_interval(distance, num_half_steps):
    return intervals[(distance, num_half_steps)]

if __name__ == '__main__':
    main()
