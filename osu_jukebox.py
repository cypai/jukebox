#!/usr/bin/env python3

import os
import subprocess
import shlex

osu_dir = "/home/cpai/Games/Games-hdd/osu/osu-dir/Songs"

def play(audio_filename):
    return subprocess.Popen(["mpv", audio_filename])

cmd = ""

while True:
    cmd = input(">> ")
    tokens = shlex.split(cmd)
    f = tokens[0]
    if f == "quit":
        exit(0)
    elif f == "test":
        sp = play(osu_dir + "/399151 Camellia - crystallized/crystallized.mp3")
        sp.wait()
    elif f == "rg":
        subprocess.run("ls " + osu_dir + " | " + cmd, shell=True)
