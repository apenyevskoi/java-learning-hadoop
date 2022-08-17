import sys

#mapper
for line in sys.stdin:
        for token in line.strip().split(" "):
            if token:
                print(token + '\t1')