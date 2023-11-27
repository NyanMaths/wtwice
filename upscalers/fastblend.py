#!/bin/python3


"""
Some weird algorithm, intended to be a simpler(by that understand less cursed) implementation of blend at the cost of a slightly smaller output image.
Author : Houmous
"""

import numpy as np


class fastblend:
    def __init__ (self):
        pass


    def scale (self, input_mat):
        h, w, _ = input_mat.shape
        upscaled_mat = np.zeros([2*h - 1, 2*w - 1, 3])


        for i in range(h):
            for j in range(w):
                upscaled_mat[2*i][2*j] = input_mat[i][j]


        for r in range(2*h - 1):
            for c in range(2*w - 1):

                if r % 2 == 1 and c % 2 == 1:
                    upscaled_mat[r][c] = np.rint((upscaled_mat[r - 1][c - 1] + upscaled_mat[r + 1][c - 1] + upscaled_mat[r - 1][c + 1] + upscaled_mat[r + 1][c + 1]) / 4.0)
                
                elif r % 2 == 1:
                    upscaled_mat[r][c] = np.rint((upscaled_mat[r - 1][c] + upscaled_mat[r + 1][c]) / 2.0)

                elif c % 2 == 1:
                    upscaled_mat[r][c] = np.rint((upscaled_mat[r][c - 1] + upscaled_mat[r][c + 1]) / 2.0)


        return np.uint8(upscaled_mat)
