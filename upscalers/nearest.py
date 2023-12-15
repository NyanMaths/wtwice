#!/bin/python3

"""
This is the most basic upscale algorithm. Excpect nothing good from it but being fast.
Author : Turbo Giga Chad
"""

import numpy as np


class nearest:
    def __init__ (self):
        pass


    def niet_scale (self, input_mat, ratio:int, denoising:int):  # do not use, does not support scaling factors
        """
        Upscales input_mat from w*h to 2w*2h and returns it in RGB/RGBA format
        Does not support either ratio and denoising, those parameters will be ignored
        """

        height, width, colours_dim = input_mat.shape
        upscaled_mat = np.zeros([2 * height, 2 * width, colours_dim], dtype=np.float32)

        for i in range(height):
            for j in range(width):
                upscaled_mat[2*i][2*j] = input_mat[i][j]
                upscaled_mat[2*i][2*j+1] = input_mat[i][j]
                upscaled_mat[2*i+1][2*j] = input_mat[i][j]
                upscaled_mat[2*i+1][2*j+1] = input_mat[i][j]

        return np.uint8(upscaled_mat)

    
    def scale (self, input_mat, ratio:int, denoising:int):
        """
        Upscales input_mat from w*h to rw*rh and returns it in RGB/RGBA format
        Does not support denoising, this parameter will be ignored
        """

        height, width, colours_dim = input_mat.shape
        upscaled_mat = np.zeros([ratio * height, ratio * width, colours_dim], dtype=np.uint8)

        for i in range(height):
            for j in range(width):
                upscaled_mat[ratio*i:ratio*(i + 1), ratio*j:ratio*(j + 1)] = np.full([ratio, ratio, colours_dim], input_mat[i][j], dtype=np.uint8)

        return upscaled_mat

    
    data_type = property(lambda object: 'mat')
