import MapReduce
import sys
from collections import Counter 

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    person = record[0]
    friend = record[1]
    mr.emit_intermediate(person,friend)
    mr.emit_intermediate(friend,person)


def reducer(key, list_of_values):
    for v in list_of_values:
      if list_of_values.count(v) == 1:
        mr.emit((key,v))

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
