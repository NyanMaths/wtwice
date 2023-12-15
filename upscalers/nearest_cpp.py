#!/bin/python3

"""
This one is a simple wrapper for a C++ implementation of Nearest, blazing fast.
No, np.upsample does not exist, that is a lie.
Wrapper : Houmous
"""

import subprocess


class nearest_cpp:
    def __init__ (self):
        pass


    def scale (self, input_picture_path:str, output_picture_path:str, ratio:int, denoising:int):
        "Just calls nearest-cpp to upscale input_picture_path to output_picture_path. Ignores denoising argument."

        subprocess.run(["upscalers/nearest-cpp", "{}".format(input_picture_path), "{}".format(output_picture_path), "{}".format(ratio)])


    data_type = property(lambda object: 'file')
