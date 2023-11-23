#!/bin/python3

"""
This module is used to probe metadata and frames from a video
in order to upscale them and re-encode them.
"""

from datetime import datetime
from platformdirs import user_cache_dir
import os
import ffmpeg


class Decoder:
    def __init__ (self, video_path):
        "Just creates the video probe using the file's path"

        self._video_path = video_path
        self._frames_directory = user_cache_dir("wtwice") + datetime.now().strftime("%d/%m/%Y %H:%M:%S")


        # Getting paths ready to call decode_chunk safely

        if not os.path.exists(user_cache_dir("wtwice")):
            os.mkdir(user_cache_dir("wtwice"))
        
        os.mkdir(_frames_directory)

        self._probe = ffmpeg.probe(video_path)
        self._stream = ffmpeg.input(video_path)


        self._stream.frames[]



    def frames_directory (self):
        return self._frames_directory

    #def decode_chunk (self):
    
