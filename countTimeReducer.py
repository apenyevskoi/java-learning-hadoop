#Reducer
#group source by time, count


import sys
import io

#input_file = open('C:/Users/INSAGNIFICANT/Downloads/R/Lorem-ipsum-dolor-sit-amet.txt', 'r', encoding = 'windows-1251')
input_file = open('C:/Users/INSAGNIFICANT/Downloads/R/test-reducer-count-time.txt', 'r', encoding = 'windows-1251')
sys.stdin = io.StringIO(input_file.read())

d = {}
while True:
    line = sys.stdin.readline()
    if not line:
        for i in d.keys():
            print(i + '\t' + str(round(d[i][0] / d[i][1])))
        break
    (key, value) = line.strip().split('\t')
    if d == {}:
        d[key] = [int(value), 1]
    else:
        if key in d:
            d[key][0] =  d[key][0] + int( value )
            d[key][1] += 1
            # print( key + '\t' + str(d[key] ))
        else:
            d[key] = [int(value), 1]
            # print( key + '\t' + str(d[key] ))
    sys.stdout.flush()