#!/bin/env python

"""
Some weird algorithm, works in a similar way to bilinear, but only upscale by a factor 2 minus 1 pixel.
It just puts a new pixel between two and computes it as the average of its neighbours.
Just use bilinear instead, this one is close to bad.
Author : Tudi
"""

import numpy as np


class Fastblend:
    def __init__ (self):
        pass


    def scale (self, input_mat, ratio:int, denoising:int):
        """
        Upscales input_mat from w*h to (2w - 1)*(2h - 1) and returns it in RGB/RGBA format
        Does not support either ratio and denoising, those parameters will be ignored
        """


        height, width, colours_dim = input_mat.shape
        upscaled_mat = np.zeros([2*height - 1, 2*width - 1, colours_dim], dtype=np.float32)

        for i in range(height):
            for j in range(width):
                upscaled_mat[2*i][2*j] = input_mat[i][j]


        for i in range(1, 2*(width-1), 2):
            upscaled_mat[:, i] = 0.5 * (upscaled_mat[:, i-1] + upscaled_mat[:, i+1])

        for j in range(1, 2*(height-1), 2):
            upscaled_mat[j, :] = 0.5 * (upscaled_mat[j-1, :] + upscaled_mat[j+1, :])


        return np.uint8(upscaled_mat)
