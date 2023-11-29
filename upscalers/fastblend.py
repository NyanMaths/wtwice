#!/bin/python3


"""
Some weird algorithm, intended to be a simpler(by that understand less cursed) implementation of blend at the cost of a slightly smaller output image.
It just puts a new pixel between two and computes it as the average of its neighbours.
Author : Houmous
"""

import numpy as np


class fastblend:
    def __init__ (self):
        pass


    def scale (self, input_mat):
        "Upscales input_mat from w*h to (2w - 1)*(2h - 1) and returns it in RGB format"

        height, width, _ = input_mat.shape
        upscaled_mat = np.zeros([2*height - 1, 2*width - 1, 3], dtype=np.float32)


        for r in range(height):
            for c in range(width):
                upscaled_mat[2*r][2*c] = input_mat[r][c]


        for r in range(1, 2*height - 1, 2):
            for c in range(1, 2*width - 1, 2):
                upscaled_mat[r][c] = np.rint((upscaled_mat[r - 1][c - 1] + upscaled_mat[r + 1][c - 1] + upscaled_mat[r - 1][c + 1] + upscaled_mat[r + 1][c + 1]) / 4.0)


        for r in range(0, 2*height - 1, 2):
            for c in range(1, 2*width - 1, 2):
                upscaled_mat[r][c] = np.rint((upscaled_mat[r][c - 1] + upscaled_mat[r][c + 1]) / 2.0)

        for r in range(1, 2*height - 1, 2):
            for c in range(0, 2*width - 1, 2):
                upscaled_mat[r][c] = np.rint((upscaled_mat[r - 1][c] + upscaled_mat[r + 1][c]) / 2.0)


        return np.uint8(upscaled_mat)
