#Combined Map and Reduce
#input text file
#output unique word and count, length of output, count of all words

import sys
import io

input_file = open('C:/Users/INSAGNIFICANT/Downloads/R/Lorem-ipsum-dolor-sit-amet.txt', 'r', encoding = 'windows-1251')
sys.stdin = io.StringIO(input_file.read())

d = {}
while True:
    line = sys.stdin.readline()
    if not line:
        print(d)
        print(len(d))
        print(sum(d.values()))
        print('break')
        break
    for token in line.strip().split(' '):
        token = token + '\t' + str(1)
        (key, value) = token.strip().split('\t')
        if d == {}:
            d[key] = int(value)
        else:
            if key in d:
                d[key] = int( d[key] ) + int( value )
                # print( key + '\t' + str(d[key] ))
            else:
                d[key] = int(value)
                # print( key + '\t' + str(d[key] ))
        sys.stdout.flush()