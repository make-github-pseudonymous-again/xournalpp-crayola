#!/usr/bin/env python3
import sys
from fmt import read
from fmt import write
from fmt import dumpXournal

columns = 1

if len(sys.argv) >= 2:
   columns = int(sys.argv[1])

colours = read(sys.stdin)

write(colours, dump=dumpXournal, columns=columns)
