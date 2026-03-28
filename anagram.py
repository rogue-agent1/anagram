#!/usr/bin/env python3
"""Anagram checker and finder."""
import sys
from collections import Counter
from itertools import permutations

def is_anagram(a, b):
    return Counter(a.lower().replace(' ','')) == Counter(b.lower().replace(' ',''))

def find_anagrams(word, wordlist):
    target = Counter(word.lower())
    return [w for w in wordlist if Counter(w.lower()) == target and w.lower() != word.lower()]

if __name__ == '__main__':
    if len(sys.argv) < 3: print("Usage: anagram.py check <word1> <word2>\n       anagram.py find <word> <wordlist_file>"); sys.exit(1)
    cmd = sys.argv[1]
    if cmd == 'check':
        a, b = sys.argv[2], sys.argv[3]
        print(f"'{a}' and '{b}' {'ARE' if is_anagram(a,b) else 'are NOT'} anagrams")
    elif cmd == 'find':
        word = sys.argv[2]
        wfile = sys.argv[3] if len(sys.argv) > 3 else '/usr/share/dict/words'
        words = open(wfile).read().splitlines()
        matches = find_anagrams(word, words)
        print(f"Anagrams of '{word}': {', '.join(matches[:20]) if matches else 'none found'}")
