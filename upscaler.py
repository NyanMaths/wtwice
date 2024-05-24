#!/bin/env python


"""
The generic class for upscaling, just name it to have it working.
It is intended to upscale by integer scale factors, do not except more anytime soon.

Author : Tudi
"""


from pathlib import Path
from PIL import Image
import numpy as np

from upscalers.nearest_cpp import *
from upscalers.dokidoki_cpp import *
from upscalers.fastblend_cpp import *
from upscalers.bilinear_cpp import *
from upscalers.wthrice import *
from upscalers.waifu2x_ncnn_vulkan import *


algorithms = \
{
    'nearest_cpp': (NearestCPP, 'file'),
    'dokidoki_cpp': (DokiDokiCPP, 'file'),
    'fastblend_cpp': (FastblendCPP, 'file'),
    'bilinear_cpp': (BilinearCPP, 'file'),
    'wthrice': (Wthrice, 'file'),
    'waifu2x_ncnn_vulkan': (Waifu2xNCNNVulkan, 'file')
}

class Upscaler:
    def __init__ (self, algorithm_name):
        self._name = algorithm_name
        self._algorithm = algorithms[algorithm_name][0]()


    def get_name (self):
        return self._name

    def get_algorithm (self):
        return self._algorithm

    def set_algorithm (self, new_algorithm_name):
        self._algorithm = upscalers[new_algorithm_name][0]()


    def upscale (self, input_picture:str, output_picture:str, ratio:int = 2, denoising:int = 0, lossless_compression:bool = True):
        if not Path(input_picture).exists(): raise FileNotFoundError("input picture not found, aborting")
        if not Path(output_picture).parent.exists(): raise FileNotFoundError("output folder not found, aborting")
        if Path(output_picture).exists(): raise FileExistsError("the requested output file already exists, I will not be responsible for this mistake")

        if algorithms[self._name][1] == 'mat':
            Image.fromarray(self.algorithm.scale(np.array(Image.open(input_picture), dtype=np.float32), ratio, denoising)).save(output_picture, None, lossless=lossless_compression)

        else:
            self.algorithm.scale(input_picture, output_picture, ratio, denoising)


    name = property(get_name)
    algorithm = property(get_algorithm, set_algorithm)
