#!/usr/bin/env python
import codecs
from os.path import isfile

def write_file(filename, content, mode = 'a+'):
    with codecs.open(filename, mode) as f:
        f.write(content)
    return

def read_file(filename, trim_ln = False):
    target = codecs.open(filename, 'r')
    if trim_ln:
        content = target.read().splitlines()
    else:
        content = target.readlines()
    target.close()
    return content

def exist(filename):
    return isfile(filename)