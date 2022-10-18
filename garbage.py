import os
import sys
import random
import hashlib


def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)


hash = hashlib.sha256()
with os.fdopen(sys.stdout.fileno(), "wb", 0) as stdout:
    for i in range(int(sys.argv[1])):
        value = random.randbytes(1024)
        stdout.write(value)
        hash.update(value)
    stdout.flush()
eprint(hash.hexdigest())
