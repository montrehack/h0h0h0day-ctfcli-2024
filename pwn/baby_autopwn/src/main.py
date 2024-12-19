#!/usr/bin/env python3

import base64
import glob
import os
import random
import sys
import subprocess
import tempfile
import time


NBINS = 256
MIN   = 16
MAX   = 4000
DELAY = 20


PROGBASE = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(PROGBASE, 'flag.txt')) as fp:
    FLAG = fp.read()


TMPLS = list(glob.glob(os.path.join(PROGBASE, '*.in')))


def crashes(inp, path):
    with subprocess.Popen([path], stdin=subprocess.PIPE, cwd='/') as io:
        io.communicate(inp)
        return -11 == io.poll()


def validate(buf, ans):
    with tempfile.TemporaryDirectory() as tmpdir:
        path = os.path.join(tmpdir, 'a.out')
        with open(path, 'wb') as fp:
            fp.write(buf)
        os.chmod(path, 0o700)

        return crashes(b'A' * (ans - 1), path) is False and crashes(b'A' * ans, path) is True


def solve(buf, ans):
    with tempfile.TemporaryDirectory() as tmpdir:
        path = os.path.join(tmpdir, 'a.out')
        with open(path, 'wb') as fp:
            fp.write(buf)

        os.chmod(path, 0o0700)

        for i in range(0, MAX):
            if crashes(b'A' * i, path):
                return i

    print('no crash?', file=sys.stderr)
    print(b64(buf))
    return 0


def b64(b):
    return base64.b64encode(b).decode()


def mkbin(n):
    with tempfile.TemporaryDirectory() as tmpdir:
        st = random.choice(TMPLS)
        #print('Using', st, file=sys.stderr)
        sd = os.path.join(tmpdir, os.path.basename(st)[:-3])
        with open(sd, 'w') as ofp:
            with open(st, 'r') as ifp:
                ofp.write(ifp.read())

        od = os.path.join(tmpdir, 'a.out')
        if sd.endswith('.c'):
            subprocess.check_output(['gcc', '-fPIC', '-w', '-fno-stack-protector', f'-DINPLEN={n}', '-o', od, sd])
        elif sd.endswith('.s'):
            od = os.path.join(tmpdir, 'a.out')
            subprocess.check_output(['as', '--defsym', f'INPLEN={n}', '-o', (od + '.o'), sd])
            subprocess.check_output(['ld', '-o', od, (od + '.o')])
        else:
            raise Exception('Internal error: unknown template')

        with open(od, 'rb') as fp:
            return fp.read()



def mkchal():
    return mkbin(random.randrange(MIN, MAX))


"""
for i in range(MIN, MAX, 8):
    o = mkbin(i)
    print(i, file=sys.stderr)
    assert(0 != solve(o, i))
exit(0)
"""

print(f'''
You are tasked to identify the precise input length required to
crash {NBINS} randomly-generated binaries. You will be given 1
base64-encoded binary at a time and will have to return the
correct input length within {DELAY} seconds.
'''.strip())
print('')


for _ in range(NBINS):
    #a, o = mkchal()
    o = mkchal()
    print(b64(o))
    t = time.time()
    u = input('Your answer> ').strip()
    u = int(u)
    if not validate(o, u):
        print('Wrong...')
        exit(0)
    if time.time() - t > DELAY:
        print('Ooooh! Right, but too late...')
        exit(0)

print(FLAG)
