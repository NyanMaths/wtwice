#!/bin/env python

"""
This is a bilinear filter, a better version of fastblend, but awfully slow because it is computed pixel-wise.
Author : Salif
"""

import numpy as np


class bilinear:
    def __init__ (self):
        pass


    def scale (self, input_mat:np.array, ratio:int, denoising:int) -> np.array:
        """
        Upscales input_mat from w*h to 2w*2h and returns it in RGB/RGBA format
        Does not support denoising, this parameter will be ignored
        """

        h, w, colours_dim = input_mat.shape
        hi = h * ratio
        wi = w * ratio

        ratio_c = (h - 1) / (hi - 1)
        out_img = np.zeros((hi, wi, colours_dim), dtype=np.float32)

        for i in range(hi):
            for j in range(wi):
                x_low, y_low = np.int64(np.floor(ratio_c * j)), np.int64(np.floor(ratio_c * i))
                x_high, y_high = np.int64(np.ceil(ratio_c * j)), np.int64(np.ceil(ratio_c * i))

                x_weight = ratio_c * j - x_low
                y_weight = ratio_c * i - y_low

                # a | b
                # -----
                # c | d
                a = input_mat[y_low, x_low]
                b = input_mat[y_low, x_high]
                c = input_mat[y_high, x_low]
                d = input_mat[y_high, x_high]

                pixel = a*(1 - x_weight)*(1 - y_weight) + b*x_weight*(1 - y_weight) + c*(1 - x_weight)*y_weight + d*x_weight*y_weight

                out_img[i, j] = pixel

        return np.uint8(out_img)


    data_type = property(lambda object: 'mat')
