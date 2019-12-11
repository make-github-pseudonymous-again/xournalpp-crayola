#!/usr/bin/env python3

def parse ( line ) :
   return tuple(map(lambda x: int(x, base=16), (line[:2], line[2:4], line[4:6])))

def stringify ( colour ) :
   return ('{:0<2x}'*3).format(*colour)

def dump ( colour , strfmt='{}', **kwargs ) :
   line = strfmt.format(stringify(colour))
   print(line, **kwargs)

def dumpXournal ( colour , file=None ) :
   dump(colour, strfmt='COLOR(0x{})', file=file, end=',')

def read ( lines ) :
   for line in lines:
      yield parse(line)

def write ( colours, dump=dump, columns=1 ) :

   table = [ [ ] for i in range(columns) ]

   for i, colour in enumerate(colours):
      table[i%columns].append(colour)

   for col in range(columns):
      if col != 0: print()
      for colour in table[col]:
         dump(colour)
