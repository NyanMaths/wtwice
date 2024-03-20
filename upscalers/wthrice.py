#!/bin/env python

"""
This is a small SRCNN trained on a gaming screenshots dataset.
In the current state of training, it does better than a bicubic algorithm.
Author : Houmous
"""

from upscalers.wthrice.srcnn import SRCNN

class wthrice:
    def __init__ (self):
        self.model = SRCNN("upscalers/wthrice/checkpoints/default-checkpoint.pt")


    def scale (self, input_picture_path:str, output_picture_path:str, ratio:int, denoising:int):
        """
        Upscales input_mat from w*h to rw*rh and returns it in RGB/RGBA format
        Does not support denoising, this parameter will be ignored
        """

        return self.model.upscale(input_picture_path, output_picture_path, ratio)

    
    data_type = property(lambda object: 'file')
