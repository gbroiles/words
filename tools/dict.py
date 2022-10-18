from codecs import unicode_escape_decode
import sys
import string
import unicodedata
import re

URLREGEXP = r"(([\da-zA-Z])([_\w-]{,62})\.){,127}(([\da-zA-Z])[_\w-]{,61})?([\da-zA-Z]\.((xn\-\-[a-zA-Z\d]+)|([a-zA-Z\d]{2,})))"
URLREGEXP = "{0}$".format(URLREGEXP)
URLSEARCH = re.compile(URLREGEXP, re.IGNORECASE)

filename = sys.argv[1]
wordlist = []

with open(filename, "r", encoding="utf8") as f:
    for line in f:
        line = unicodedata.normalize("NFKC", line).encode("ASCII", "ignore").decode()
        line = line.strip()
        line = line.translate({ord(i): i for i in string.ascii_letters})
        line = [word.strip(string.punctuation + string.digits) for word in line.split()]
        for word in line:
            if (
                (word not in wordlist)
                and (len(word) > 1)
                and (word.upper() != word)
                and not (re.match(URLSEARCH, word.lower().strip()))
            ):
                print(word, end=" ", flush=True)
