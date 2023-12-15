#!/bin/python3

"""
This one is a simple wrapper for a C++ implementation of Bilinear, blazing fast.
Wrapper : Houmous
"""

import subprocess


class bilinear_cpp:
    def __init__ (self):
        pass


    def scale (self, input_picture_path:str, output_picture_path:str, ratio:int, denoising:int):
        "Just calls bilinear-cpp to upscale input_picture_path to output_picture_path. Ignores denoising argument."

        subprocess.run(["upscalers/bilinear-cpp", "{}".format(input_picture_path), "{}".format(output_picture_path), "{}".format(ratio)])


    data_type = property(lambda object: 'file')
