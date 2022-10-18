import os, sys

with open(0, "rb", 0) as infile:
    target = infile.read()

print(f"Read {len(target)} characters.")

for i in range(256):
    if i != target[i]:
        print(f"Something wrong at {i}, {target[i]}")
        sys.exit(1)
print("256 bytes read OK.")
sys.exit(0)
