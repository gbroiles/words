import random
import sys

WORDLIST = "american-english-small"

def wordvalue(word):
    total = 0
    for letter in word:
        total += ord(letter)
    return(total % 256)

words = []
word_lookup = {}
with open(WORDLIST,"r") as file:
    for word in file:
        if word.find("'") != -1:
            continue
        word = word.strip()
        total = wordvalue(word)
        words.append((word, total))

for word, value in words:
    try:
        temp_list = word_lookup[value]
        temp_list.append(word)
        word_lookup[value] = temp_list
    except KeyError:
        word_lookup[value] = [word]

index = random.randint(0,len(words)+1)
target = words[index][0]
print("Target = ",target)

result = []
word = target
value = wordvalue(target)
print(f"Word: {word}, Value: {value}")
for letter in word:
    print(letter)
    letter_value = ord(letter)
    print(letter_value, end=' ')
    candidates = word_lookup[letter_value]
    print(f"Length: {len(candidates)}")
    if len(candidates) == 0:
        print("Len was 0!")
        sys.exit(0)
    possible = len(candidates) - 1
    selected = random.randint(0,possible)
    print(f"[{ord(letter)}], {possible}, {selected}", end=' ')
    print(candidates[selected])
    result.append(candidates[selected])
print(word)
output = ""
for entry in result:
    print(chr(wordvalue(entry)),entry)
    output = output + chr(wordvalue(entry))
print(output)
sys.exit(0)
