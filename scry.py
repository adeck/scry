#!/usr/bin/env python2

import math

def byte_frequencies(stream):
  from collections import Counter
  return Counter(stream)

# gives the number of bits of entropy per byte;
#   so, a value from 0-8, inclusive.
# frequencies is a Counter object from the collections package
# length is an integer
def shannon_entropy(frequencies, length):
  entropy = 0.0
  for _, count in frequencies.most_common():
    p = 1.0 * count / length
    # lgN is the logarithm with base 2
    if p > 0:
      entropy -= p * math.log(p, 2) 
  return entropy

def get_histogram(frequencies):
  import matplotlib.pyplot as plot
  plot.bar(xrange(0,256), [frequencies[i] for i in xrange(256)])
  return plot

def get_bitmap(stream):
  import Image
  length = len(stream)
  dim = int(math.ceil(math.sqrt(length)))
  img = Image.new('RGB', (dim,dim), "black") # create a new black image
  pixels = img.load()
  for i in xrange(length):    # for every byte
    v = stream[i]
    pixels[i // dim, i % dim] = (v, v, v)
  return img

class Scry:
  def __init__(self, filename):
    self.filename = filename
  
  def temp_main(self):
    result = {}
    with open(self.filename, 'rb') as f:
      stream = bytearray(f.read())
      freq = byte_frequencies(stream)
      entropy = shannon_entropy(freq, len(stream))
      print 'num unique bytes present:', len(freq)
      print 'entropy:', entropy
      get_histogram(freq).show()
      get_bitmap(stream).show()


if __name__ == '__main__':
  Scry('scry.py').temp_main()



