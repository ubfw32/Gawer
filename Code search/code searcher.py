import re
import os
import datetime
import time
import math
from pathlib import Path

dir = Path()


# pattern search in texts
def searcher(dir):
    print(f"Search date: [{datetime.date.today()}]")
    print(f"FILE\t\t\t\tSERIAL N°\n"
          f"-------\t\t\t\t----------")
    num = 0

    for dirs, subdirs, files in os.walk(dir):
        for txt in files:
            rute = os.path.join(dirs, txt)
            file = open(rute, 'r')
            content = file.read()
            file.close()
            codes = re.findall(r'N\D{3}-\d{5}', content)
            for results in codes:
                print(f'{txt}\t\t{results}')
                num += 1

    print(f"\n\nFinded numbers: {num}")


# measure the time from start to end of ejecution
start = time.time()
searcher(dir)
end = time.time()
duration = end - start

# program duration print
print(f"\n\nSearch duration: {math.ceil(duration)} seconds")


