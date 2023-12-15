#!/bin/python3

"""
This one is a simple wrapper for a C++ implementation of Fastblend, blazing fast.
Wrapper : Houmous
"""

import subprocess


class fastblend_cpp:
    def __init__ (self):
        pass


    def scale (self, input_picture_path:str, output_picture_path:str, ratio:int, denoising:int):
        "Just calls fastblend-cpp to upscale input_picture_path to output_picture_path. Ignores denoising and ratio arguments."

        subprocess.run(["upscalers/fastblend-cpp", "{}".format(input_picture_path), "{}".format(output_picture_path)])


    data_type = property(lambda object: 'file')