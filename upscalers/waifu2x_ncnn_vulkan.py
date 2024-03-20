#!/bin/env python

"""
This one is a simple wrapper for waifu2x-ncnn-vulkan, something probably better than anything we can do.
Wrapper : Houmous
"""

import subprocess
from shutil import which


class waifu2x_ncnn_vulkan:
    def __init__ (self):
        pass


    def scale (self, input_picture_path:str, output_picture_path:str, ratio:int, denoising:int):
        "Just calls waifu2x to upscale input_picture_path to output_picture_path"

        if not ratio in [2, 4, 8]: raise ValueError("Allowed scale factors : 2, 4, 8\nAborting process")
        if not denoising in [-1, 0, 1, 2, 3]: raise ValueError("Please choose a correct denoising factor between -1, 0, 1, 2, 3.\nAborting for now...")

        subprocess.run(["waifu2x-ncnn-vulkan", "-i", "{}".format(input_picture_path), "-o", "{}".format(output_picture_path), "-s", "{}".format(ratio), "-n", "{}".format(denoising)])


    data_type = property(lambda object: 'file')
