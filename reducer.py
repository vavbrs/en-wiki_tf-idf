#!/usr/bin/env python
import sys

#with open("corpus_size.txt", "r") as f:
#    corpus_size = int(f[0])
corpus_size = 20000000
top_count = 20
total_count = 0
top = []

def comparator(value1, value2):
    res = value1[1] - value2[1]
    if res == s0:
        return -value1[0].compareTo(value2[0])
    return -res
    
for line in sys.stdin:
    total_count += 1
    
    data = line.split('\t')
    term = data[0]
    value = data[1].split()
    
    top.append(value)
    top.sort(cmp=comparator)
    if len(top) > top_count:
        del top[-1]


coef = log(corpus_size) - log(total_count)
print term + "\t",
for docid, tf in top:
    print "%s:%s\t" % (docid, tf * coef),
print 
