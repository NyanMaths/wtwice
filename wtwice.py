#!/bin/env python

import encoder
import processing
import decoder
import sys


class WTwice:
    def __init__ (self):
        self.args = dict()
        self.args['-i'] = ''
        self.args['-o'] = ''
        self.args['-r'] = 2
        self.args['-n'] = 0
        self.args['-u'] = 'waifu2x_ncnn_vulkan'

        if len(sys.argv) % 2 == 0:
            raise RuntimeError("Wrong number of command-line arguments, please fix ur computer grammar.")

        i = 1
        while i < len(sys.argv):
            if sys.argv[i] in ('-i', '-o', '-r', '-n', '-u'):
                self.args[sys.argv[i]] = sys.argv[i + 1]

            else:
                print(f"Unknown argument {sys.argv[i]}, it will be ignored\n")

            i += 2

        if (self.args['-i'] == '' or self.args['-o'] == ''):
            raise RuntimeError("Please specify both input and output media path with the arguments -i and -o")


        self._decoder = decoder.Decoder(self.args['i'])
        self._upscaler = processing.FramesProcessor(self.args['-u'], self.args['-r'], self.args['-n'], _decoder.frames_directory())
        self._encoder = encoder.Encoder(self.args['-o'])



    def start (self):
        


if __name__ == "__main__":
    # launch upscaler with given command-line arguments because me too lazy to code a proper GUI
    
    app = WTwice()
    app.start()
