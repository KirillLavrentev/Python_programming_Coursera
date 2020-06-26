
import sys

digit_string = sys.argv[1]
s = 0
for i in range(0,len(digit_string)):
    s = s + int(digit_string[i])

print(s)
