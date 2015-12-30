#!/usr/bin/env python
import sys
from collections import Counter


for line in std.stdin:
    data = line.split('\t')
    content = data[1].lower().split()
    counter = Counter(content)
    
    words = counter.keys()
    counts = counter.values()
    
    for i in len(words):
        print "%s\t%s %s" % (words[i], docid, counts[i])