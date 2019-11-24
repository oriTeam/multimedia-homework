#!/usr/bin/python3

import numpy as np
from scipy.io import wavfile

RATE = 44100
ROOT_FREQUENCY = 440
TONE_LENGTH = 1
SCALE = 1.059463

def main():
    # time length for a file
    time = np.linspace(0, TONE_LENGTH, RATE * TONE_LENGTH)

    try :
        first_note = ROOT_FREQUENCY * 1 / (np.power(SCALE, 9))
        tone = np.sin(first_note * 2 * np.pi * time)
        print('Generating file {}.wav with frequency {}'.format(0, first_note))
        wavfile.write('storage/0.wav', RATE, tone)

        upper_boundary = ROOT_FREQUENCY * np.power(SCALE, 3)

        current_note = first_note
        count = 0
        while current_note * SCALE <= upper_boundary:
            count = count + 1
            current_note = current_note * SCALE
            tone = np.sin(current_note * 2 * np.pi * time)
            print('Generating file {}.wav with frequency {}'.format(count, current_note))
            wavfile.write('storage/{}.wav'.format(count), RATE, tone)

    except Exception as e:
        print(str(e))
    else:
        print('Done without any error!')

if __name__ == "__main__":
    main()
