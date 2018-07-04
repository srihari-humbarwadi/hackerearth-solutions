import sys
for line in sys.stdin:
    if line == '':
        break
    comment = False
    if '//' not in line:
        result = line.replace('->', '.')
    else:
        commentIndex = line.index('//')
        result = line[0:commentIndex].replace('->', '.') + line[commentIndex:]
    print(result)
