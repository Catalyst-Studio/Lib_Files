import time
from easylib.progressBar import progressbar
for i in progressbar(range(1100), "Computing: ", 100):
    time.sleep(.01) # any code you need