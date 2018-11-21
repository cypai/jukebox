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
    audio_filenames = list(filter(lambda d: "mp3" in d or "ogg" in d, os.listdir(osu_dir + "/" + song_dir)))
    if len(audio_filenames) > 0:
        file_pairs = sorted(list(map(lambda f: (os.stat(osu_dir + "/" + song_dir + "/" + f).st_size, f), audio_filenames)), reverse=True)
        sp = play(osu_dir + "/" + song_dir + "/" + file_pairs[0][1])

song_history = ""
cmd = ""

while True:
    cmd = input(">> ")
    tokens = shlex.split(cmd)
    f = tokens[0]
    if f == "q":
        exit(0)
    elif f == "rg":
        subprocess.run("ls " + osu_dir + " | rg -i " + " ".join(tokens[1:]), shell=True)
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
        subprocess.run("ls " + osu_dir + " | rg -i " + " ".join(tokens[1:]), shell=True)
        try:
            while True:
                song_dirs = list(filter(lambda d: " ".join(tokens[1:]).lower() in d.lower(), os.listdir(osu_dir)))
                random_dir = random.choice(song_dirs)
                play_dir(random_dir)
                song_history = random_dir
        except:
            pass
    elif f == "prg":
        dirs = list(filter(lambda d: " ".join(tokens[1:]).lower() in d.lower(), os.listdir(osu_dir)))
        if len(dirs) == 0:
            print("No songs matching search query found")
        else:
            subprocess.run("ls " + osu_dir + " | rg -i " + " ".join(tokens[1:]), shell=True)
            try:
                while len(dirs) > 0:
                    choice = random.choice(dirs)
                    dirs.remove(choice)
                    play_dir(choice)
                    song_history = choice
            except:
                pass
    elif f == "a":
        play_dir(song_history)
