import MapReduce
import sys
from collections import Counter 

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    sequence_id = record[0]
    nucleotides = record[1][:-10]
    mr.emit_intermediate(nucleotides,1)

def reducer(key, list_of_values):
    mr.emit((key))
# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
