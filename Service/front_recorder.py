#!/usr/bin/env python

import subprocess
import datetime

now = datetime.datetime.now()
filename = now.strftime("%Y%m%d_%H%M%S")

subprocess.call("/opt/vc/bin/raspivid -w 960 -h 540 -n -hf -vf -o /home/camera/front/record{0}.h264 -t 1000000".format(filename).split())
