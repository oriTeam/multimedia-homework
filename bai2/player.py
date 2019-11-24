#!/usr/bin/python3

import getopt
import sys

from playsound import playsound


def main(argv):
    try:
        opts, args = getopt.getopt(argv, "hi:a", ["all=", "one="])
    except getopt.GetoptError:
        print('Wrong syntax')
        print('Please run "python3 player.py -h" to see the usage')
        sys.exit(2)

    for opt, arg in opts:
        if opt == '-h':
            print("-- To play a file, run: 'python3 player.py -i <input_file_name>'")
            print("-- To play all file, run: 'python3 player.py -a'")
            print("-- To stop playing, just press Ctrl + C (on both Linux and Mac)")
            sys.exit()
        elif opt in ("-a", "--all"):
            while True:
                print('NOTE: To stop playing, just press Ctrl + C (on both Linux and Mac)')
                for i in range(0,13):
                    print('Playing {}.wav'.format(i))
                    playsound('./storage/{}.wav'.format(i))
        elif opt in ("-i", "--one"):
            input_file = arg

            # support call only file name
            if "storage" not in arg:
                input_file = "./storage/" + arg

            print('NOTE: To stop playing, just press Ctrl + C (on both Linux and Mac)')
            try:
                while True:
                    playsound(input_file)
            except Exception:
                print('File not found. Please check your path')

if __name__ == "__main__":
    main(sys.argv[1:])