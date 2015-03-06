lines = []
lines += [line.replace('\n', ' ').split(' ') for line in open('test.sents')]


print (lines[0])
