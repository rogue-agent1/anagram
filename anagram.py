#!/usr/bin/env python3
"""anagram - Anagram utilities."""
import sys,argparse,json
from collections import Counter
from itertools import permutations
def is_anagram(a,b):
    return Counter(a.lower().replace(" ",""))==Counter(b.lower().replace(" ",""))
def find_anagrams(word,wordlist):
    target=Counter(word.lower())
    return [w for w in wordlist if Counter(w.lower())==target and w.lower()!=word.lower()]
def main():
    p=argparse.ArgumentParser(description="Anagram tool")
    sub=p.add_subparsers(dest="cmd")
    c=sub.add_parser("check");c.add_argument("a");c.add_argument("b")
    f=sub.add_parser("find");f.add_argument("word");f.add_argument("--dict",help="Word list file")
    args=p.parse_args()
    if args.cmd=="check":
        print(json.dumps({"a":args.a,"b":args.b,"is_anagram":is_anagram(args.a,args.b)}))
    elif args.cmd=="find":
        if args.dict:
            with open(args.dict) as f:words=f.read().split()
        else:words=["listen","silent","heart","earth","angel","angle","evil","vile","live"]
        matches=find_anagrams(args.word,words)
        print(json.dumps({"word":args.word,"anagrams":matches,"count":len(matches)}))
    else:p.print_help()
if __name__=="__main__":main()
