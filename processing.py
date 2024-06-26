#!/bin/env python

import os
import subprocess
from pathlib import Path
from upscaler import *


class FramesProcessor:
    "upscales everything inside the cache directory following the given settings"

    def __init__ (self, upscaler_name:str, ratio:int = 2, denoising_strength:int = 1, frames_directory:str = "/var/wtwice", verbose:bool = False):
        self._upscaler = Upscaler(upscaler_name)
        self._ratio = ratio
        self._denoising = denoising_strength
        self._working_directory = frames_directory
        self._verbose = verbose


    def upscale_working_directory (self, begin:int, end:int):
        for frame_path in [f"{self._working_directory}/frame-{begin + i}.png" for i in range(end - begin)]:
            self._upscaler.upscale(frame_path, os.path.join(_working_directory, os.path.basename(frame_path) + "-u" + Path(frame_path).suffix), self._ratio, self._denoising)

            Path(frame_path).unlink()  # removes the processed frame once upscaled

            if (self._verbose): print("upscaled frame {}\n".format(frame_path))


        if (self._verbose): print("finished upscaling chunk")
