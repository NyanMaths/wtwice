#!/bin/env python

import os
import imageio.v3 as iio
import io


class Encoder:
    def __init__ (self, output_path):
        "initializes the output file"
        if not os.path.exists(os.path.dirname(output_path)):
            raise FileNotFoundError("output folder does not exist, terminating program")
        
        self._output_path = output_path


    def encode_frames (begin:int, end:int):
        iio.
