#!/bin/python3


"""
The generic class for upscaling, just name it and it will obey
A little bit unsafe though, just do not rm -rf /
Please do not

We only programmed it to upscale by two, do not excpect more anytime soon.
"""


from pathlib import Path
import cv2

from upscalers.nearest import *


class Upscaler:
    def __init__ (self, name:string):
        self._name = name

        self._algorithm = eval(name + "()")  # unsafe as hell


    def get_name (self):
        return self._name

    def get_algorithm (self):
        return self._algorithm

    def set_algorithm (self, new_algorithm:str):
        self._algorithm = eval(name + "()")


    def upscale (input_picture:str, output_picture:str):
        if not Path(input_picture).exists(): raise OSError("Input picture not found, aborting...")
        if not Path(output_picture).parent().exists(): raise OSError("Output folder not found, aborting...")


        # remember kids : do not nest your code unless you want to push unreadable and undebuggable garbage to your repo
        if not cv2.imwrite(output_picture, self.algorithm.scale(cv2.imread(input_picture))): raise OSError("something prevented the image to be scaled, check your access rights")


    name = property(get_name)
    algorithm = property(get_algorithm, set_algorithm)