import os, sys

with os.fdopen(sys.stdout.fileno(), "wb", 0) as stdout:
    for value in range(256):
        stdout.write(value.to_bytes(1,sys.byteorder,signed=False))
    stdout.flush()
