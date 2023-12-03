from datetime import datetime
from time import sleep
import sys

seconds = int(sys.argv[-1])


def sec(count: int):
    while count:
        print(f'{datetime.now()} seconds\n')
        sleep(1)
        count -= 1


sec(seconds)
