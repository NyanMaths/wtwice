#!/bin/env python


from sys import argv

if len(argv) != 5:
    raise RuntimeError("invalid use : call using wthrice.py input_path output_path scale_factor model_path")


from srcnn import SRCNN

print("upscaling input...\n")

model = SRCNN(argv[4])
model.upscale(argv[1], argv[2], float(argv[3]))
