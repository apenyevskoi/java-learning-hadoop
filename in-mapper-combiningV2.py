import sys
import io

d = {}
while True:
    line = sys.stdin.readline()
    if not line:
        for i in d.keys( ):
            print( i + '\t' + str( d[i] ) )
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