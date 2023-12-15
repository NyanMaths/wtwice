#!/bin/python3

"""
This is just a test script to show the capabilities of our upscale algorithms compared to other ones. waifu2x goes brrrrrr
Importajt notice : use this script only in wtwice directory if you do not want your filesystem to get wrecked !

Just create a folder inside wtwice named tests, make another one with the name of your dataset
and put the same picture at different sizes (currently 128, 256, 512 and 1024 pixels height)

Folder template :
tests
|-- grandma-smiling
|   |-- 128.webp 
|   |-- 256.webp
|   |-- 512.webp
|   |-- 1024.webp
|
|-- there-s-a-stray-cat-outside
|   |-- 128.webp 
|   |-- 256.webp
|   |-- 512.webp
|   |-- 1024.webp


Author : Houmous
"""

from pathlib import Path
from PIL import Image
import numpy as np
from upscaler import *


# this one is intended to compare outputs in terms of sharpness, meaning the average of gradient's norm
def sharpness (picture_path:str):
    picture = Image.open(picture_path).convert('L')
    picture_matrix = np.asarray(picture, dtype=np.uint8)

    gy, gx = np.gradient(picture_matrix)
    return np.average(np.sqrt(gx*gx + gy*gy))



dataset = input("Which dataset do you want to upscale ? ")

if not Path("tests/" + dataset).exists():
    raise FileNotFoundError("Impossible to find the dataset to upscale, aborting")


codec = input("What is your file's format (you better use webp) ? ")


# Stores the upscaler's name and the upscale ratios to proceed with
ratios = \
{
    'nearest_cpp': [2, 4],
    'dokidoki_cpp': [2],
    'fastblend_cpp': [2],
    'bilinear_cpp': [2, 4],
    'waifu2x_ncnn_vulkan': [2, 4]
}
test_resolutions = ('128', '256', '512', '1024')

for upscaler_name in ratios.keys():
    if input("Do you want to run {} ? [Y/n] ".format(upscaler_name)) in ('n', 'N'):
        continue

    for res in test_resolutions:
        upscale_directory = "tests/" + dataset + "/" + res
        if not Path(upscale_directory).exists(): Path(upscale_directory).mkdir()

        u = Upscaler(upscaler_name)

        for ratio in ratios[upscaler_name]:
            if not Path(upscale_directory + "/{}".format(ratio)).exists(): Path(upscale_directory + "/{}".format(ratio)).mkdir()
            u.upscale(upscale_directory + "." + codec, upscale_directory + "/{}/".format(ratio) + upscaler_name + "." + codec, ratio=ratio)


if input("\nDo you want to compare images' sharpness ? [Y/n] ") in ('n', 'N'): exit(0)

for res in test_resolutions:
    for ratio in ratios[upscaler_name]:
        comparsion_directory = "tests/" + dataset + "/" + res + "/{}".format(ratio)
        
        with open(comparsion_directory + "/sharpness-comparsion", 'w') as comparsion_output:
            for algorithm in ratios.keys():
                picture_path = comparsion_directory + "/" + algorithm + "." + codec

                if Path(picture_path).exists():
                    comparsion_output.write(algorithm + " : {}\n".format(sharpness(picture_path)))
