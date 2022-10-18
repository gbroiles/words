# words

This set of programs will translate a binary file into words, and decode a file thus encoded back into binary.

For example:

`python3 words.py american-english-small.txt < testfile.bin > testfile.txt`

will encode the "testfile.bin" file as a series of words taken from the file "american-english-small.txt" and write the result to "testfile.txt".

and this invocation:

`python3 unwords.py < testfile.txt > testfile.out`

will decode the "testfile.txt" file back into its binary equivalent and write it to disk as testfile.out.

The programs operate on STDIN and STDOUT so they can be used as part of a pipeline, e.g. -

`sha256sum testfile.bin && python3 words.py american-english-small.txt < testfile.bin > testfile.txt`

will run the program sha256sum on the source file before encoding it; and

`python3 unwords.py < testfile.txt | sha256sum`

feeds the output to sha256sum to verify that the file has been processed unchanged. 

This can be done with a single command:

`sha256sum testfile.bin && python3 words.py american-english-small.txt < testfile.bin | python3 unwords.py | sha256sum`

Note that the resulting text form of the original file will be much larger than the original file, though it should compress relatively well as it's standard text. The degree of expansion will depend on the dictionary file used.

Any file can be used to provide words for the conversion - for example, 

`python3 words.py holmes.txt < testfile.bin > testfile.txt`

will use "The Adventures of Sherlock Holmes" by Arthur Conan Doyle as the source for words to be used.

Note that access to the dictionary is *not* required to decode the file; the value of a word is calculated as follows:

`(ord(letter 1) + ord(letter 2) + ord(letter ..)) % 256`

For example, the value of "cat" would be:

`(ord("c") + ord("a") + ord("t")) % 256`

which is the same as 

`(99 + 97 + 116) % 256`

.. or `56`. 

This means that any number of words can map to a given byte in the original file. Also note that "CAT" and "cat" and "Cat" will have 3 different values. 

The files holmes.txt is from the Gutenberg Project and is public domain to the best of my knowledge.

The file american-english-small.txt is from /usr/share/dict on a Ubuntu 16.04 installation. 


