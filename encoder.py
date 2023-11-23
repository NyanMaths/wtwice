#!/bin/python3

import os


class Encoder:
    def __init__ (self, output_path):
        "Just initializes the output file"
        if not os.path.exists(os.path.dirname(output_path)):
            raise FileNotFoundError("Output folder does not exist, terminating program")
        
        self._output_path = output_path