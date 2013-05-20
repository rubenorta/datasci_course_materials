import MapReduce
import sys

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    key = record[0]
    mr.emit_intermediate(key,1)

def reducer(key, list_of_values):
    number_of_friends = 0
    for v in list_of_values:
      number_of_friends += 1
    mr.emit((key,number_of_friends))

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
