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


class Upscaler:
    def __init__ (self, name:str):
        self._name = name

        self._algorithm = eval(name + "()")  # unsafe as hell


    def get_name (self):
        return self._name

    def get_algorithm (self):
        return self._algorithm

    def set_algorithm (self, new_algorithm:str):
        self._algorithm = eval(name + "()")


    def upscale (self, input_picture:str, output_picture:str):
        if not Path(input_picture).exists(): raise OSError("Input picture not found, aborting...")
        if not Path(output_picture).parent.exists(): raise OSError("Output folder not found, aborting...")
        if Path(output_picture).exists(): raise OSError("The requested output file already exists, I do not want to be responsible for your mistakes, get crashed.")


        # remember kids : do not nest code unless you want to commit unreadable and undebbuggable garbage on your repos
        Image.fromarray(self.algorithm.scale(np.array(Image.open(input_picture), dtype=np.uint8))).save(output_picture, None, lossless=True)


    name = property(get_name)
    algorithm = property(get_algorithm, set_algorithm)