#!/bin/python3

"""
This is a small SRCNN trained on a gaming screenshots dataset.
In the current state of training, it does better than a bicubic algorithm.
Author : Houmous
"""

from upscalers.nn.srcnn import SRCNN

class wthrice:
    def __init__ (self):
        self.model = SRCNN("wthrice/checkpoints/weights-8_7.9_5.pt")


    def scale (self, input_mat, ratio:int, denoising:int):
        """
        Upscales input_mat from w*h to rw*rh and returns it in RGB/RGBA format
        Does not support denoising, this parameter will be ignored
        """

        return model.upscale_matrices([input_mat], ratio)

    
    data_type = property(lambda object: 'mat')
