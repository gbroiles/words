import random
import sys
import unicodedata
import re
import string
import fileinput
import os
import hashlib


def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)


def wordvalue(word):
    total = 0
    for letter in word:
        total += ord(letter)
    return total % 256


def build_lookup(filename):
    URLREGEXP = r"(([\da-zA-Z])([_\w-]{,62})\.){,127}(([\da-zA-Z])[_\w-]{,61})?([\da-zA-Z]\.((xn\-\-[a-zA-Z\d]+)|([a-zA-Z\d]{2,})))"
    URLREGEXP = "{0}$".format(URLREGEXP)
    URLSEARCH = re.compile(URLREGEXP, re.IGNORECASE)
    words = {}
    word_lookup = {}
    with open(filename, "r", encoding="utf8") as f:
        for line in f:
            line = (
                unicodedata.normalize("NFKC", line).encode("ASCII", "ignore").decode()
            )
            line = line.strip()
            line = line.translate({ord(i): i for i in string.ascii_letters})
            line = [
                word.strip(string.punctuation + string.digits) for word in line.split()
            ]
            for word in line:
                if (
                    (word not in words.keys())
                    and (len(word) > 1)
                    and (word.upper() != word)
                    and not (re.match(URLSEARCH, word.lower().strip()))
                ):
                    words[word] = wordvalue(word)

    for word, value in words.items():
        try:
            temp_list = word_lookup[value]
            temp_list.append(word)
            word_lookup[value] = temp_list
        except KeyError:
            word_lookup[value] = [word]
    for i in range(256):
        if len(word_lookup[1]) > 0:
            continue
        else:
            eprint(f"Dictionary problem, no word found for byte {i}")
    return word_lookup


def build_text(target, lookuptable):
    result = []
    for letter in target:
        candidates = lookuptable[letter]
        if len(candidates) == 0:
            print(f"No candidates for [character {letter}]!")
            sys.exit(1)
        possible = len(candidates) - 1
        selected = random.randint(0, possible)
        result.append(candidates[selected])
    return result


word_lookup = {}
word_lookup = build_lookup(sys.argv[1])


with open(0, "rb", 0) as infile:
    target = infile.read()
if target == "":
    target = "The quick brown fox jumps over the lazy dog."
    print("No input received, using '{target}'")

eprint(f"Read {len(target)} bytes, SHA256: {hashlib.sha256(target).hexdigest()}")

result = build_text(target, word_lookup)

output = ""
for entry in result:
    print(entry, end=" ")
print()
sys.exit(0)
