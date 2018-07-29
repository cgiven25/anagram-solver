#!/usr/bin/python3
from time import time, sleep
from platform import system
from subprocess import Popen

def main():
    try:
        print("Loading dictionary...")
        start = time()
        wordsFile = open("words.txt")
        words = wordsFile.read().splitlines()
        print("Loaded in {} seconds.".format(time() - start))
        print()

        while 1:
            letters = list(input("Letters: "))
            print("Finding anagrams...")
            print()

            anagrams = []
            for word in words:
                # Need a copy of the array so the original list isn't edited
                currentLetters = letters[:]
                anagram = True
                for letter in word:
                    if letter not in currentLetters:
                        anagram = False
                        break
                    currentLetters.remove(letter)
                if anagram:
                    anagrams.append("".join(word))

            # Sorts the list of anagrams.  The key is a function that returns the length of the elements.
            # Sorted in ascending order so I had to reverse them.
            anagrams.sort(key = lambda s: len(s))
            anagrams.reverse()

            for word in anagrams:
                print(word)

            print()
            input("Press enter to find more anagrams.")

            # Clears the screen between uses
            if system() == "Windows":
                Popen("cls")
            else:
                Popen("clear")

            # Give time for the subprocess to launch and finish
            sleep(.25)

    except KeyboardInterrupt:
        exit(0)
    # FileNotFoundError does not exist in Python 2 so I have to use the base class
    except EnvironmentError:
        print("Dictionary could not be found.")
        exit(0)

if __name__ == "__main__":
    main()