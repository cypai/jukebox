#!/usr/bin/env python3

import readline # enables history, etc. in input()
import os
import subprocess
import shlex
import random

osu_dir = "/home/cpai/Games/Games-hdd/osu/osu-dir/Songs"

def play(audio_filename):
    return subprocess.run(["mpv", audio_filename], encoding="UTF-8")

def play_dir(song_dir):
    audio_filenames = list(filter(lambda d: "mp3" in d, os.listdir(osu_dir + "/" + song_dir)))
    if len(audio_filenames) > 0:
        sp = play(osu_dir + "/" + song_dir + "/" + audio_filenames[0])

song_history = ""
cmd = ""

while True:
    cmd = input(">> ")
    tokens = shlex.split(cmd)
    f = tokens[0]
    if f == "q":
        exit(0)
    elif f == "rg":
        subprocess.run("ls " + osu_dir + " | " + cmd, shell=True)
    elif f == "p":
        song_dirs = list(filter(lambda d: d.split(" ")[0] == tokens[1], os.listdir(osu_dir)))
        if len(song_dirs) > 0:
            play_dir(song_dirs[0])
            song_history = song_dirs[0]
    elif f == "pr":
        song_dirs = os.listdir(osu_dir)
        random_dir = random.choice(song_dirs)
        play_dir(random_dir)
        song_history = random_dir
    elif f == "lpr":
        try:
            while True:
                song_dirs = os.listdir(osu_dir)
                random_dir = random.choice(song_dirs)
                play_dir(random_dir)
                song_history = random_dir
        except:
            pass
    elif f == "lprg":
        for d in list(filter(lambda d: tokens[1] in d, os.listdir(osu_dir))):
            print(d)
        try:
            while True:
                song_dirs = list(filter(lambda d: tokens[1] in d, os.listdir(osu_dir)))
                random_dir = random.choice(song_dirs)
                play_dir(random_dir)
                song_history = random_dir
        except:
            pass
    elif f == "prg":
        dirs = list(filter(lambda d: tokens[1] in d, os.listdir(osu_dir)))
        if len(dirs) == 0:
            print("No songs matching search query found")
        else:
            if len(dirs) == 1:
                play_dir(dirs[0])
            else:
                print("Multiple songs found. List:")
                subprocess.run("ls " + osu_dir + " | rg " + " ".join(tokens[1:]), shell=True)
                print("Playing randomly chosen:")
                play_dir(random.choice(dirs))
    elif f == "a":
        play_dir(song_history)
