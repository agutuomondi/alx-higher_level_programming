#!/usr/bin/python3
import shutil
import os

def append_after(filename="", search_string="", new_string=""):
    temp_filename = filename + ".temp"

    with open(filename, "r") as infile, open(temp_filename, "w") as outfile:
        for line in infile:
            outfile.write(line)
            if search_string in line:
                outfile.write(new_string)

    shutil.move(temp_filename, filename)
