#!/bin/env python

"""
This algorithm takes the average of two pixels to put between them in order to get a smoother result
Not incredible, but still better than nearest for larger images.
Now worky, faster than fastblend(...), but much more blurry result.
Author : Turbo Giga Chad
"""

import numpy as np


class dokidoki:
    def __init__ (self):
        pass


    def scale (self, m, ratio:int, denoising:int):
        """
        Upscales input_mat from w*h to 2w*2h and returns it in RGB/RGBA format
        Does not support either ratio and denoising, those parameters will be ignored
        """

        h, w, colours_dim = m.shape
        n = h
        upscaled_mat = np.zeros([2 * h, 2 * w, colours_dim], dtype=np.float32)

        #valeurs fixes - coins
        upscaled_mat[0][0] = m[0][0]
        upscaled_mat[0][2*w-1] = m[0][w-1]
        upscaled_mat[2*h-1][0] = m[h-1][0]
        upscaled_mat[2*h-1][2*w-1] = m[h-1][w-1]

        #valeurs des bordures - moyenne à 2
        for j in range(n - 1):
            valr1 = (m[0][j] + m[0][j+1])/2         #1ere ligne
            valc1 = (m[j][0] + m[j+1][0])/2         #1ere colonne
            valr2 = (m[n-1][j] + m[n-1][j+1])/2     #derniere ligne
            valc2 = (m[j][n-1] + m[j+1][n-1])/2     #dernier colonne

            #premiere ligne
            upscaled_mat[0][2*j+1] = valr1
            upscaled_mat[0][2*(j+1)] = valr1

            #premiere colonne
            upscaled_mat[2*j+1][0] = valc1
            upscaled_mat[2*(j+1)][0] = valc1

            #derniere ligne
            upscaled_mat[2*n-1][2*j+1] = valr2
            upscaled_mat[2*n-1][2*(j+1)] = valr2

            #derniere colonne
            upscaled_mat[2*j+1][2*n-1] = valc2
            upscaled_mat[2*(j+1)][2*n-1] = valc2

        #valeurs intérieures - moyenne à 4
        for i in range(h-1):
            for j in range(w-1):
                val_bloc = (m[i][j] + m[i+1][j] + m[i][j+1] + m[i+1][j+1])/4

                upscaled_mat[2*i+1][2*j+1] = val_bloc
                upscaled_mat[2*i+1][2*(j+1)] = val_bloc
                upscaled_mat[2*(i+1)][2*j+1] = val_bloc
                upscaled_mat[2*(i+1)][2*(j+1)] = val_bloc

        return np.uint8(upscaled_mat)


    data_type = property(lambda object: 'mat')