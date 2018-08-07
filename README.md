# Anagram Solver
Takes given letters and determines what words can be made from them.
The dictionary provided is [this one](https://raw.githubusercontent.com/dwyl/english-words/master/words_alpha.txt), but any list of words will work as long as it is named words.txt (or the code is edited appropriately). 

## Usage
```python3 anagramSolver.py``` or ```./anagramSolver.py```

./ can be replaced with the path to the script if it is not in your current directory.
If you plan on using this frequently I recommend you put it in your /usr/bin folder and setting an alias.  This lets you use it from anywhere with just the name of the script (or whatever you set the alias to).  You also need to move the dictionary.
If you are using Python 2, you will need to change the comment at the top of the script to reflect your current python version (changing it to ```#!/usr/bin/python``` should work).

After a dictionary is loaded you will be prompted for letters to find anagrams for.  If you want to leave a character unspecified (to increase the length of the words without knowing what letters they are), use a "?" character.  When it is finished searching it will give a list of all words in the dictionary that are some combination and subset of those letters.  These are sorted by length starting with the longest words because I imagine this will be most frequently used for word games.

This will run forever until you close it.  For Linux, it's usually Ctrl+C; for Windows, Ctrl+Z.
