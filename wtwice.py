#!/bin/python3

import encoder
import processing
import decoder
import sys


class WTwice:
    def __init__ (self):
        self._decoder = decoder.Decoder(sys.argv[1])
        self._upscaler = processing.FramesProcessor(sys.argv[3], sys.argv[4], sys.argv[5], _decoder.frames_directory())
        self._encoder = encoder.Encoder(sys.argv[2])


    def start (self):
        


if __name__ == "__main__":
    # launch upscaler
    
    app = WTwice()
    app.start()



