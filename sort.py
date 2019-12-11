#!/usr/bin/env python3
import fileinput
from fmt import read
from fmt import write
from hilbert import Hilbert_to_int

colours = read(fileinput.input())

write(sorted(colours, key = Hilbert_to_int))
