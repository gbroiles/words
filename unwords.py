from multiprocessing.sharedctypes import Value
import os
import sys
import hashlib


def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)


source = sys.stdin.read()

count = 0
hash = hashlib.sha256()
with os.fdopen(sys.stdout.fileno(), "wb", 0) as stdout:
    for word in source.split():
        value = 0
        for letter in word:
            value += ord(letter)
        value = value % 256
        value = value.to_bytes(1, "big")
        stdout.write(value)
        count += 1
        hash.update(value)
    stdout.flush()
eprint(f"\nSaw {count} bytes, SHA256: {hash.hexdigest()}")
