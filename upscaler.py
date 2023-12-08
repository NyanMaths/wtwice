#!/bin/python3


"""
The generic class for upscaling, just name it and it will obey
A little bit unsafe though, just do not rm -rf /
Please do not

We only programmed it to upscale by two, do not excpect more anytime soon.
"""


from pathlib import Path
from PIL import Image
import numpy as np

from upscalers.nearest import *
from upscalers.dokidoki import *
from upscalers.fastblend import *
from upscalers.bilinear import *
from upscalers.waifu2x_ncnn_vulkan import *


class Upscaler:
    def __init__ (self, name:str):
        self._name = name

        self._algorithm = eval(name + "()")  # unsafe as hell, yolo


    def get_name (self):
        return self._name

    def get_algorithm (self):
        return self._algorithm

    def set_algorithm (self, new_algorithm:str):
        self._algorithm = eval(name + "()")


    def upscale (self, input_picture:str, output_picture:str, ratio:int = 2, denoising:int = 0, lossless_compression:bool = True):
        if not Path(input_picture).exists(): raise FileNotFoundError("Input picture not found, aborting...")
        if not Path(output_picture).parent.exists(): raise FileNotFoundError("Output folder not found, aborting...")
        if Path(output_picture).exists(): raise FileExistsError("The requested output file already exists, I do not want to be responsible for your mistakes, get crashed.")

        if self.algorithm._type == 'mat':
            # remember kids : do not nest code unless you want to commit unreadable and undebuggable garbage on your repos
            Image.fromarray(self.algorithm.scale(np.array(Image.open(input_picture), dtype=np.float32), ratio, denoising)).save(output_picture, None, lossless=lossless_compression)

        else:
            self.algorithm.scale(input_picture, output_picture, ratio, denoising)


    name = property(get_name)
    algorithm = property(get_algorithm, set_algorithm)
