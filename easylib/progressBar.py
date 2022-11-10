import sys, time
from datetime import datetime


def progressbar(it, prefix: str = "", size: int = 60, out=sys.stdout):  # Python3.3+
    itemsList = ["▏", "▎", "▍", "▌", "▋", "▊", "▉", "█"]
    print(itemsList)
    count = len(it)
    startTime = datetime.now()
    barSize = 0
    def show(j, barSize):
        x = int(size * j / count)
        if barSize < x:
            barSize = x
            for char in itemsList:
                print("\r{}[{}{}] {}% {:.01f}s".format(prefix, "█" * (x-1) + char, " " * (size - x), int((j/count)*100), (datetime.now()-startTime).total_seconds() * 10**3 / 1000), file=out, flush=True, end='')
                time.sleep(.0001)
        else:
            print(
                "\r{}[{}{}] {}% {:.01f}s".format(prefix, "█" * x, " " * (size - x), int((j / count) * 100),
                                                 (datetime.now() - startTime).total_seconds() * 10 ** 3 / 1000),
                file=out, flush=True, end='')
        return barSize

    barSize = show(0, barSize)
    for i, item in enumerate(it):
        yield item
        barSize = show(i + 1, barSize)
    print("\n", flush=True, file=out)
