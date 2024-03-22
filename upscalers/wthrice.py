#!/bin/env python

"""
This is a small SRCNN trained on a gaming screenshots dataset (https://www.kaggle.com/datasets/aditmagotra/gameplay-images).
In the current state of training, it does better than a bicubic algorithm.
Author : Tudi
"""

from upscalers.srcnn.srcnn import SRCNN

class Wthrice:
    def __init__ (self):
        self.model = SRCNN("upscalers/wthrice/checkpoints/default-checkpoint.pt")


    def scale (self, input_picture_path:str, output_picture_path:str, ratio:int, denoising:int):
        """
        Upscales input_mat from w*h to rw*rh and returns it in RGB format, no alpha channel
        Does not support denoising, this parameter will be ignored
        """

        self.model.upscale(input_picture_path, output_picture_path, ratio)
