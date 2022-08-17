import sys
import io

input_file = open('C:/Users/INSAGNIFICANT/Downloads/R/python_100mln_lines.txt', 'r', encoding = 'windows-1251')
sys.stdin = io.StringIO(input_file.read())

d = {}
while True:
    line = sys.stdin.readline()
    if not line:
        print(d)
        print(sum(d.values()))
        print('break')
        break
    (key, value) = line.strip().split('\t')
    if d == {}:
        d[key] = value
    else:
        if key in d:
            d[key] = int( d[key] ) + int( value )
            # print( key + '\t' + str(d[key] ))
        else:
            d[key] = value
            # print( key + '\t' + str(d[key] ))
    sys.stdout.flush()