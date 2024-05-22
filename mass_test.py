#!/usr/bin/env python

from pathlib import Path
from PIL import Image
import numpy as np
from upscaler import *

# this one is intended to compare outputs in terms of sharpness, meaning the average of gradient's norm
def sharpness (picture_path:str):
    picture = Image.open(picture_path).convert('L')
    picture_matrix = np.asarray(picture, dtype=np.uint8)

    (gy, gx) = np.gradient(picture_matrix)
    return np.average(np.sqrt(gx*gx + gy*gy))


def peak_signal_to_noise_ratio (picture_path:str, target_picture_path:str):
    picture = Image.open(picture_path).convert('L')
    target_picture = Image.open(target_picture_path).convert('L')
    picture_matrix = np.asarray(picture, dtype=np.float32) / 255.0
    target_picture_matrix = np.asarray(target_picture, dtype=np.float32) / 255.0


    squared_differences = np.square(picture_matrix - target_picture_matrix)
    
    (n, m) = np.shape(squared_differences)
    return -np.log(np.sum(squared_differences) / (n * m))


dataset = "tests/.mass-test/dataset"

# Stores the upscaler's name and the upscale ratios to proceed with
upscaler_names = \
(
    'nearest_cpp',
    'bilinear_cpp',
    'wthrice',
    'waifu2x_ncnn_vulkan'
)
test_resolutions = (80, 160)
test_ratios = (2, 4)

#for upscaler_name in upscaler_names:
#    print(f"running {upscaler_name}...\n")

#    u = Upscaler(upscaler_name)

#    for ratio in test_ratios:
#        for res in test_resolutions:
#            original_directory = f"tests/.mass-test/dataset/{res}"
#            upscale_directory = f"tests/.mass-test/upscaled-dataset/{ratio}/{upscaler_name}/{res*ratio}"

#            for i in range(1, 1001):
#                u.upscale(f"{original_directory}/{i}.png", f"{upscale_directory}/{i}.png", ratio=ratio)


print("running sharpness test...\n")
with open(f"tests/.mass-test/average-sharpness", 'w') as sharpness_output:
    for upscaler_name in upscaler_names:
        for ratio in test_ratios:
            for res in test_resolutions:
                print(f"running sharpness test for {upscaler_name}, ratio {ratio}, original {res}px width")
                
                upscaled_directory = f"tests/.mass-test/upscaled-dataset/{ratio}/{upscaler_name}/{res*ratio}"

                cumulator = 0.0
                for i in range(1, 1001):
                    cumulator += sharpness(f"{upscaled_directory}/{i}.png")

                sharpness_output.write(f"{upscaler_name} from {res}px, factor {ratio} : {cumulator / 1000.0}\n")


print("running PSNR test...\n")
with open(f"tests/.mass-test/average-psnr", 'w') as psnr_output:
    for upscaler_name in upscaler_names:
        for ratio in test_ratios:
            for res in test_resolutions:
                print(f"running PSNR test for {upscaler_name}, ratio {ratio}, original {res}px width")
                
                original_directory = f"tests/.mass-test/dataset/{res*ratio}"
                upscaled_directory = f"tests/.mass-test/upscaled-dataset/{ratio}/{upscaler_name}/{res*ratio}"

                cumulator = 0.0
                for i in range(1, 1001):
                    cumulator += peak_signal_to_noise_ratio(f"{upscaled_directory}/{i}.png", f"{original_directory}/{i}.png")

                psnr_output.write(f"{upscaler_name} from {res}px, factor {ratio} : {cumulator / 1000.0}\n")
