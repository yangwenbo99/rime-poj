import unicodedata
import csv

def n(x, l, tone):
    r = x[:l+1] + tone + x[l+1:]
    return unicodedata.normalize('NFC', r)

def pg(o, l, t):
    print(n(o, l, ''), t + '1', sep='\t')
    print(n(o, l, chr(0x301)), t + '2', sep='\t')
    print(n(o, l, chr(0x300)), t + '3', sep='\t')
    print(n(o, l, ''), t + '4', sep='\t')
    print(n(o, l, chr(0x302)), t + '5', sep='\t')
    print(n(o, l, chr(0x30C)), t + '6', sep='\t')
    print(n(o, l, chr(0x304)), t + '7', sep='\t')
    print(n(o, l, chr(0x30D)), t + '8', sep='\t')

with open('../data/vowels.csv', 'r') as f:
    reader = csv.DictReader(f)
    for row in reader:
        o, t, l = row['Original'].strip(), row['Typed in'].strip(), int(row['Location'])
        pg(o, l, t)
        pg(o.upper(), l, t.upper())
        if len(o) > 1:
            pg(o.capitalize(), l, t.capitalize())
