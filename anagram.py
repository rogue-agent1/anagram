#!/usr/bin/env python3
"""Anagram finder and checker."""
import sys
from collections import Counter
def is_anagram(a, b):
    return Counter(a.lower().replace(" ","")) == Counter(b.lower().replace(" ",""))
def find_anagrams(word, wordlist):
    key = tuple(sorted(word.lower()))
    return [w for w in wordlist if tuple(sorted(w.lower())) == key and w.lower() != word.lower()]
if __name__ == "__main__":
    if len(sys.argv) == 3:
        a, b = sys.argv[1], sys.argv[2]
        print(f"'{a}' and '{b}': {'ANAGRAM' if is_anagram(a, b) else 'not anagram'}")
    elif len(sys.argv) == 2:
        word = sys.argv[1]
        try:
            words = open("/usr/share/dict/words").read().split()
        except FileNotFoundError:
            words = ["listen","silent","evil","vile","heart","earth","least","steal","tales"]
        matches = find_anagrams(word, words)
        print(f"Anagrams of '{word}': {matches[:20]}")
    else:
        print("Usage: anagram.py <word1> [word2]")
