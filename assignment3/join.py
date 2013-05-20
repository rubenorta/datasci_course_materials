import MapReduce
import sys

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    key = record[1]
    mr.emit_intermediate(key,record)

def reducer(key, list_of_values):
    head = list_of_values[0]
    for pos in range(1,len(list_of_values)):
      list = head + list_of_values[pos]  
      mr.emit(list)

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
