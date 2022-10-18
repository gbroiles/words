import sys, hashlib
with open(sys.argv[1],"rb") as infile:
    target = infile.read()
print(hashlib.sha256(target).hexdigest())