#!/usr/bin/env python

import subprocess
#import datetime

#now = datetime.datetime.now()
#dirname = now.strftime("%Y%m%d_%H%M%S")

#subprocess.call("mkdir /home/camera/rear/{}".format(dirname).split())
subprocess.call("motion".split(), cwd="/home/camera/rear/")
