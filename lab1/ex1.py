#!/usr/bin/env python3
# SUTD 50.042 FCS Lab 1
# Simple file read in/out

# Done by Han Xing Yi (1004330) in collaboration with Velusamy Sathiakumar Ragul Balaji (1004101)

# Import libraries
import sys
import argparse
import string


def doStuff(filein, fileout, key, mode):
    output = ""
    # PROTIP: pythonic way
    with open(filein, mode="r", encoding="utf-8", newline="\n") as fin:
        text = fin.read()
        # do stuff
        for char in text:
            if char in string.printable:
                if mode == 'e':
                    output += string.printable[ (string.printable.index(char) + key ) % len(string.printable) ]
                elif mode == 'd':
                    output += string.printable[ (string.printable.index(char) - key ) % len(string.printable) ]
            else:
                print("Error: Input char is not in string.printable")
                
    with open(fileout, mode="w", encoding="utf-8", newline="\n") as fout:
        fout.write(output)


# our main function
if __name__ == "__main__":
    # set up the argument parser
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", dest="filein", help="input file", type=str,required=True)
    parser.add_argument("-o", dest="fileout", help="output file", type=str, required=True)
    parser.add_argument("-k", dest="key", help="key", type=int, choices=range(1, len(string.printable)), required=True)
    parser.add_argument("-m", dest="mode", help="mode (d/e)", type=str, choices=['d', 'e'],required=True)

    # parse our arguments
    args = parser.parse_args()
    filein = args.filein
    fileout = args.fileout
    key = args.key
    mode = args.mode

    doStuff(filein, fileout, key, mode)

    # all done
