import MapReduce
import sys
import re
from collections import OrderedDict

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    # key: document identifier
    # value: document contents
    document = record[0]
    value = record[1]
    words = value.split()
    for w in words:
      mr.emit_intermediate(w,document)

def reducer(key, list_of_values):
    mr.emit((key, list(set(list_of_values))))

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
