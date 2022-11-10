import time
from easylib.progressBar import progressbar
for i in progressbar(range(79), "Computing: ", 190):
    time.sleep(.01) # any code you need