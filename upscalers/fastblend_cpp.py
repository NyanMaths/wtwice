#!/bin/env python

"""
This one is a simple wrapper for a C++ implementation of fastblend, blazing fast.
Wrapper : Tudi
"""

import subprocess


class FastblendCPP:
    def __init__ (self):
        pass


    def scale (self, input_picture_path:str, output_picture_path:str, ratio:int, denoising:int):
        "Just calls fastblend-cpp to upscale input_picture_path to output_picture_path. Ignores denoising and ratio arguments."

        subprocess.run(["upscalers/fastblend-cpp", "{}".format(input_picture_path), "{}".format(output_picture_path)])
