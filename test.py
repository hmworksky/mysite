#!/usr/bin/python
import commands
import os
t2 = os.system('ps -ef')
title = commands.getoutput('pwd')
t3 = os.popen('ls')
print t3
