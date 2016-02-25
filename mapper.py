#!/usr/bin/env python
import sys
from collections import Counter

# halo

for line in sys.stdin:
    data = line.split('\t')
    
    docid = int(data[0])
    content = data[1].lower().split()
    
    counter = Counter(content)
    words = counter.keys()
    sys.stdout.flush()
    counts = counter.values()
    
    for i in range(len(words)):
        print "%s\t%s %s" % (words[i], docid, counts[i])