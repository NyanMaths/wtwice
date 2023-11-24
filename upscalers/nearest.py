#!/bin/python3


"""
This is the most basic upscale algorithm. Excpect nothing good from it.
Author : Turbo Giga Chad
"""

import numpy as np


class nearest:
    def __init__ (self):
        pass


    def scale (self, mat):
        h, w, _ = mat.shape
        upscaled_mat = np.zeros([2 * h, 2 * w, 3], dtype=np.uint8)

        for i in range(h):
            for j in range(w):
                val = np.array(mat[i, j], dtype=np.uint8)
                upscaled_mat[2*i][2*j] = val
                upscaled_mat[2*i][2*j+1] = val
                upscaled_mat[2*i+1][2*j] = val
                upscaled_mat[2*i+1][2*j+1] = val

        return upscaled_mat