#!/usr/bin/env python3
import fileinput
from fmt import read
from fmt import write
from colour import is_pastel

colours = read(fileinput.input())

write(filter(is_pastel, colours))
