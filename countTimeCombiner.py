#Combiner
#group source by time, count


import sys
import io

#input_file = open('C:/Users/INSAGNIFICANT/Downloads/R/Lorem-ipsum-dolor-sit-amet.txt', 'r', encoding = 'windows-1251')
input_file = open('C:/Users/INSAGNIFICANT/Downloads/R/test-combiner-count-time.txt', 'r', encoding = 'windows-1251')
sys.stdin = io.StringIO(input_file.read())

d = {}
while True:
    line = sys.stdin.readline()
    if not line:
        for i in d.keys():
            print(i + '\t' + str(round(d[i][0])) + ';' + str(d[i][1]))
        break
    (key, two_values) = line.strip().split('\t')
    (time_value, count_value) = two_values.split(';')
    if d == {}:
        d[key] = [int(time_value), 1]
    else:
        if key in d:
            d[key][0] =  d[key][0] + int( time_value )
            d[key][1] += 1
            # print( key + '\t' + str(d[key] ))
        else:
            d[key] = [int(time_value), 1]
            # print( key + '\t' + str(d[key] ))
    sys.stdout.flush()