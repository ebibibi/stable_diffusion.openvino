import sys
import subprocess
import datetime

args = sys.argv

while True:
    filename = '/tmp/output/' + datetime.datetime.now().strftime('%Y%m%d_%H%M%S') + '.png'
    subprocess.run("python3 /src/demo.py --output " + filename + " --prompt \"" + args[1] + "\"", shell=True)
