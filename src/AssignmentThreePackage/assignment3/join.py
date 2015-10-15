import MapReduce
import sys

"""
Word Count Example in the Simple Python MapReduce Framework
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    # key: document identifier
    # value: document contents
    key = record[1]
    value = record
#    lineitem = value.split()
#    key = record[1]
#    value = record[1]
          
    #words = value.split()
    #print (key, value)
    #for w in words:
    mr.emit_intermediate(key, value)

def reducer(key, list_of_values):
    # key: word
    # value: list of occurrence counts
    
    for v in range(1, len(list_of_values)):
        key = list_of_values[0]
        value = list_of_values[v]
        mr.emit((key, value))
    #print key
    #print list_of_values

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
