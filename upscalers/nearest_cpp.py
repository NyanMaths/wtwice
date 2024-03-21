#!/bin/env python

"""
This one is a simple wrapper for a C++ implementation of nearest, blazing fast.
Litteraly the same as torch.upsample, this algorithm is the most basic possible in upscaling.
Wrapper : Tudi
"""

import subprocess


class NearestCPP:
    def __init__ (self):
        pass


    def scale (self, input_picture_path:str, output_picture_path:str, ratio:int, denoising:int):
        "Just calls nearest-cpp to upscale input_picture_path to output_picture_path. Ignores denoising argument."

        subprocess.run(["upscalers/nearest-cpp", "{}".format(input_picture_path), "{}".format(output_picture_path), "{}".format(ratio)])
