#!/usr/bin/python3
for i in range(ord('a'), ord('{')):
    if i == ord('e') or i == ord('q'):
        continue
    else:
        print('{:c}'.format(i), end="")
