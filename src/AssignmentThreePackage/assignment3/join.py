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
    #old_list = list_of_values
    testkey = '32'
    testorder = 'order' + ' 32' + ' Descripton for Order 32'
    testline = str([u'line', u'32', u'Order 32 + Line1'])
    test_list_of_values = []
    test_list_of_values.append(testorder)
    test_list_of_values.append(testline)
    print test_list_of_values
    print (key, list_of_values)
    
    #testkey = testorder[1]
    #print(list_of_values)
    #newkey = list_of_values[0]
    #listlength = len(list_of_values)
    #for x in range(1,listlength):
    #for x in range(0,len(list_of_values)):
    mr.emit((testkey, test_list_of_values))
    #print str(rkey)
    #print key
    #print list_of_values

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
