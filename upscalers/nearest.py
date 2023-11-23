#!/bin/python3

"""
This is the most basic upscale algorithm. Excpect nothing good from it.
"""


class nearest:
    def __init__ (self):
        pass


    def scale (mat):
        n = len(mat)
        m2 = [[0 for j in range(2*n) ] for _ in range(2*n)]

        for i in range(n):
            for j in range(n):
                val = mat.item((i, j))
                m2[2*i][2*j] = val
                m2[2*i][2*j+1] = val
                m2[2*i+1][2*j] = val
                m2[2*i+1][2*j+1] = val

        mat2 = np.matrix(m2)
        return mat2