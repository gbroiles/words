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
        #        print(f"Initial size: {len(line)}")
        line = unicodedata.normalize("NFKC", line).encode("ASCII", "ignore").decode()
        #        print(type(line))
        #        print(f"ASCIIfy: {len(line)}")
        line = line.strip()
        #        print(f"After .strip(): {len(line)}")
        line = line.translate({ord(i): i for i in string.ascii_letters})
        #        print(f"After ASCII strip: {len(line)}")
        line = [word.strip(string.punctuation + string.digits) for word in line.split()]
        for word in line:
            if (
                (word not in wordlist)
                and (len(word) > 1)
                and (word.upper() != word)
                and not (re.match(URLSEARCH, word.lower().strip()))
            ):
                print(word, end=" ", flush=True)
#                wordlist.append(word)
#            else:
#                print(f"[{word}]",end =' ',flush=True)
#        print()
#        input()
