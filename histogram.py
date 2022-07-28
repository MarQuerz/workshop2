import sys
import string

words = sys.stdin.read().split()

for i in range (0,12,2):
    print(f'{words[i]}            [{int(words[i+1])*"**"}]   {int(words[i+1])*9}%')