#!/bin/env python

"""
This is a bilinear filter, a better version of fastblend, but slower because it is computed pixel-wise.
Author : Salif
"""

import numpy as np


class Bilinear:
    def __init__ (self):
        pass


    def scale (self, input_mat:np.array, ratio:int, denoising:int) -> np.array:
        """
        Upscales input_mat from w*h to 2w*2h and returns it in RGB/RGBA format
        Does not support denoising, this parameter will be ignored
        """

        n, m, colours_dim = img.shape
        n2, m2 = n*r, m*r    #output image's size (n2 x m2)
        r_i = (n - 1)/(n2 - 1)      #inverse ratio (-1 to stay in the indexes interval) for n dimension
        r_j = (m - 1)/(m2 - 1)      #inverse ratio for m dimension
        img_scale = np.zeros((n2, m2, colours_dim), dtype=np.float32)


        for i in range(n2):
            for j in range(m2):
                x = r_j*j       #abscissa value calculation
                y = r_i*i       #ordinate value calculation
                xf, yf = np.int64(np.floor(x)), np.int64(np.floor(y))   #floor value of x and y
                xc, yc = np.int64(np.ceil(x)), np.int64(np.ceil(y))     #ceil value of x and y
                wx, wy = x - xf, y - yf     #weights associated with x (wx) and y (wy) values

                val_g = (1 - wy)*img[yf][xf] + wy*img[yf][xc]   #left linear interpolation on y coordinate
                val_d = (1 - wy)*img[yc][xf] + wy*img[yc][xc]   #right linear interpolation on x coordinate

                val = (1 - wx)*val_g + wx*val_d     #linear interpolation on x coordinate / final value
                img_scale[i][j] = val

        return np.uint8(img_scale)
