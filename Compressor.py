#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2021 arijit <arijit@linux-inspiron-5567>
#
# Distributed under terms of the MIT license.

import subprocess


class App:

    def __init__(self, input_file, output_file):

        self.input = input_file
        self.output = output_file
        self.FFmpeg = "/usr/bin/ffmpeg"  # change the location based on your machine 

    def audioCompress(self):

        a_codec = "libvorbis" # change the encoder if you know a better one
        a_command = [self.FFmpeg, "-i", self.input, "-c:a", a_codec, "-b:a", "128k", self.output]
        if subprocess.run(a_command).returncode == 0:
            print(f"{self.input} has been converted successfully !!")

        else:
            print(f"Something went wrong with {self.input}")

    def videoCompress(self):

        v_codec = "libx265" # change the encoder if you know a better one 
        v_command = [self.FFmpeg, "-i", self.input, "-map", "0", "-c:v", v_codec, "-an", self.output]
        if subprocess.run(v_command).returncode == 0:
            print(f"{self.input} has been converted successfully !!")

        else:
            print(f"Something went wrong with {self.input}")

    def audiovisualCompress(self):
        a_codec = "libvorbis" # change the encoder if you know a better one
        v_codec = "libx265"   # change the encoder if you know a better one
        av_command = [self.FFmpeg, "-i", self.input, "-map", "0", "-c:v", v_codec, "-c:a", a_codec, "-b:a", "128k", self.output]
        if subprocess.run(av_command).returncode == 0:
            print(f"{self.input} has been converted successfully !!")

        else:
            print(f"Something went wrong with {self.output}")    

if (__name__=="__main__"):
    file_in = input("Provide the file path :")
    file_out = input("Provide the file path where the output will be saved :")
    root = App(file_in, file_out)
    try:
        video_file = (".mp4", ".mkv", ".webm", ".flv", ".vob", "ogv", ".gif", ".gifv", ".avi", ".wmv", ".mov", ".yuv", ".rm", ".m4v", ".mpv", ".3gp", ".wav")
        if file_in.endswith(video_file):
            asktyp = input("Do you want video stream only in your output(Extracts video only) ?(y/n)")
            if asktyp == "y":
                root.videoCompress()
            else:
                root.audiovisualCompress()

        else:
            root.audioCompress()      

    except:
        print("Something Went Wrong !!")             


            



