import MapReduce
import sys

"""
Word Count Example in the Simple Python MapReduce Framework
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    # key: person
    # value: friend
    #key = record[0]   
    #key=record[1]
    print record
    #mr.emit_intermediate(key, record)
      

def reducer(key, list_of_values):
    # key: word
    # value: list of occurrence counts
    #print key
    #print list_of_values
    #print '\n'
    #print (key, list_of_values)
    total = 0
    #for v in list_of_values:
         #total += v
    #mr.emit((key,list_of_values))

# Do not modify below this line
# =============================
if __name__ == '__main__':
    inputdata = open(sys.argv[1])
    mr.execute(inputdata, mapper, reducer)
