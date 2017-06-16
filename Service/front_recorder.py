#!/usr/bin/env python

import os
import subprocess


# Make new file name
all_files = os.listdir('/home/camera/front/')
current_numbers = []
for file_name in all_files:
    current_numbers.append(int(file_name[:-5]))
current_numbers.sort()
if (current_numbers):
    next_number = current_numbers[-1] + 1
else:
    next_number = 0
new_filename = "{}".format(next_number)

# Check disk space
if (current_numbers):
    remove_number = current_numbers[0]
    p = subprocess.Popen("df -h".split(), stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=False)
    disk_space = int(p.stdout.readlines()[1].split()[4][:-1])
    if (80 < disk_space):
        subprocess.call("rm /home/camera/front/{}.h264".format(remove_number).split())

subprocess.call("/opt/vc/bin/raspivid -w 960 -h 540 -n -hf -vf -o /home/camera/front/{0}.h264 -t 1000000".format(new_filename).split())
