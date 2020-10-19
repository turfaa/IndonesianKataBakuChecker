#!/usr/bin/python3

# Author    : Turfa Auliarachman
# Date      : October 23, 2016

from IndonesianKataBakuChecker.BakuChecker import *
import sys
import os.path

dictFile = os.path.dirname(os.path.realpath(__file__))+"/IndonesianKataBakuCheckerTest/dict.txt"
checkerList = []

print("#"*70)
print("# Indonesian Kata Baku Checker" + " "*39 + "#")
print("# Author   : Turfa Auliarachman" + " "*38 + "#")
print("# Date     : October 23, 2016" + " "*40 + "#")
print("#"*70)
print()

if (len(sys.argv)!=2):
    print("Usage:")
    print("{} <path-to-file>".format(sys.argv[0]))
else:
    checkerList.append(BakuChecker(dictFile))

    if (not(os.path.exists(sys.argv[1]))):
        print("File {} not found.".format(sys.argv[1]))
    else:
        f = open(sys.argv[1]).readlines()
        for i in range(0, len(f)):
            errList = []

            if (f[i][len(f[i])-1]=="\n"):
                f[i] = f[i][:-1]

            for checker in checkerList:
                errList += checker.check(f[i])
            for err in errList:
                print("Checker       : {}".format(err.checkerDescription))
                print("Line          : {}".format(i+1))
                print("Original text : {}".format(err.original))
                print("Message       : {}".format(err.message))
                print()
