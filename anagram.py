#!/usr/bin/env python3
"""anagram - Check anagrams, generate from letters. Zero deps."""
import sys, itertools, collections
def is_anagram(a, b):
    return sorted(a.lower().replace(" ","")) == sorted(b.lower().replace(" ",""))
def find_anagrams(word, wordlist):
    key = sorted(word.lower())
    return [w for w in wordlist if sorted(w.lower()) == key and w.lower() != word.lower()]
def main():
    if len(sys.argv) < 2:
        print("Usage: anagram.py <check a b | find word [wordlist]>"); sys.exit(1)
    cmd = sys.argv[1]
    if cmd == "check":
        a, b = sys.argv[2], sys.argv[3]
        print(f"{'✓ Anagram' if is_anagram(a, b) else '✗ Not anagram'}: {a} / {b}")
    elif cmd == "find":
        word = sys.argv[2]
        wl = open(sys.argv[3]).read().split() if len(sys.argv) > 3 else open("/usr/share/dict/words").read().split()
        results = find_anagrams(word, wl)
        print(f"Anagrams of '{word}': {', '.join(results[:20])}" if results else "None found")
if __name__ == "__main__": main()
