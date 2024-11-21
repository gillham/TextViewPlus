import os
import pathlib
import datetime
import subprocess
import sys

myfile = ".build"
mybuild = 0
mydate = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")

myrun = subprocess.run(["C:\\Users\\paul\\Me\\Tools\\TMPx\\windows-i386\\tmpx.exe", "build.asm", "-l", "build.l"], check=False)

with open(myfile, "r", encoding=None) as f:

    data = f.read()
    mybuild = int(data)

mybuild += 1

with open(myfile, "w", encoding=None) as f:
    f.write(str(mybuild))

print(sys.argv)

MAKE_OPTION = "none"

if len(sys.argv) > 1:
    MAKE_OPTION = sys.argv[1]

MSG = " If you don't like to read, you haven't  found the right book! - J.K Rowling"
MSG_FILE = 'msg.txt'

if MAKE_OPTION == 'none':
    MSG = f"Build {mybuild} on {mydate}"

print(MSG)

with open(MSG_FILE, "w", encoding=None) as f:
    f.write(MSG)


