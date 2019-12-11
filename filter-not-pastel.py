#!/usr/bin/env python3
import fileinput
from fmt import read
from fmt import write
from colour import is_pastel
from itertools import filterfalse

colours = read(fileinput.input())

write(filterfalse(is_pastel, colours))
