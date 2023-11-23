#!/bin/python3

import os
import subprocess
from shutils import which
from pathlib import Path


class Upscaler:
    "Basically upscales everything inside the cache directory following the given settings"

    def __init__ (self, upscaler:str = "waifu2x_ncnn_vulkan", ratio:int = 2, denoising_strength:int = 1, frames_directory:str = "/var/wtwice", verbose:bool = False):
        if not ratio in [2, 4, 8]: raise ValueError("Allowed scale factors : 2, 4, 8\nAborting process")
        if which(upscaler) is None: raise RuntimeError("Unknown upscale tool, check your PATH variable or spelling")
        if not denoising in [-1, 0, 1, 2, 3]: raise ValueError("Please choose a correct denoising factor between -1, 0, 1, 2, 3.\nAborting for now...")
        # Frames path existence check not necessary, already checked during frames decoding 0.000001 seconds earlier


        self._upscaler = upscaler
        self._ratio = ratio
        self._denoising = denoising_strength
        self._working_directory = frames_directory
        self._verbose = verbose

    
    def upscale_working_directory (self):
        for frame_path in [os.path.realpath(filename) for filename in os.listdir(self._working_directory)]:
            subprocess.run([self.upscaler + " -i \"{}\" -o \"{}\" -s {} -n {}".format(frame_path, os.path.join(_working_directory, os.path.basename(frame_path) + "-u" + Path(frame_path).suffix), self._ratio, self._denoising)])

            Path(frame_path).unlink()  # removes the processed frame once upscaled

            if (self._verbose): print("Upscaled frame {}\n".format(frame_path))


        if (self._verbose): print("Finished upscaling chunk")
