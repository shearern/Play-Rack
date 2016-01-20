#!/usr/bin/python
'''Find and compile Qt ui files'''

import os
import sys
import subprocess

def python_path():
    return os.path.dirname(sys.executable)

def uic_path():
    path = os.path.join(python_path(), 'Scripts')
    for filename in os.listdir(path):
        if filename.lower().startswith('pyside-uic'):
            return os.path.join(path, filename)
    print "Couldn't find pyside-uic"
    sys.exit(2)

def rcc_path():
    path = os.path.join(python_path(), 'Lib', 'site-packages', 'PySide')
    if os.path.exists(path):
        for filename in os.listdir(path):
            if filename.lower().startswith('pyside-rcc'):
                return os.path.join(path, filename)
    print "Couldn't find pyside-rcc"
    sys.exit(2)


class Compiler(object):
    def __init__(self, bin_path):
        self.bin_path = bin_path
    def compile(self, src, dst):
        try:
            subprocess.check_output(
                args=(
                    self.bin_path,
                    src,
                    '-o', dst,
                ))
        except subprocess.CalledProcessError as e:
            print e


if __name__ == '__main__':

    uic = Compiler(uic_path())
    rcc = Compiler(rcc_path())

    src = os.path.abspath(os.path.dirname(__file__))
    for dirpath, dirnames, filenames in os.walk(src):
        for filename in filenames:
            path = os.path.join(dirpath, filename)

            if filename.endswith('.ui'):
                dst = path[:-3] + '.py'
                print "%s -> %s" % (path, dst)
                uic.compile(path, dst)

            if filename.endswith('.qrc'):
                dst = path[:-4] + '_rc.py'
                print "%s -> %s" % (path, dst)
                rcc.compile(path, dst)
