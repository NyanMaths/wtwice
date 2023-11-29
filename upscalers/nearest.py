#!/bin/python3

"""
This is the most basic upscale algorithm. Excpect nothing good from it but being fast.
Author : Turbo Giga Chad
"""

import numpy as np


class nearest:
    def __init__ (self):
        pass


    def scale (self, mat):
        "Upscales mat from w*h to 2w*2h and returns it in RGB format"

        height, width, _ = mat.shape
        upscaled_mat = np.zeros([2 * height, 2 * width, 3], dtype=np.float32)

        for i in range(height):
            for j in range(width):
                upscaled_mat[2*i][2*j] = mat[i][j]
                upscaled_mat[2*i][2*j+1] = mat[i][j]
                upscaled_mat[2*i+1][2*j] = mat[i][j]
                upscaled_mat[2*i+1][2*j+1] = mat[i][j]

        return np.uint8(upscaled_mat)
