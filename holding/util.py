import csv, json
from collections import OrderedDict

from io import StringIO, BytesIO
# StringIO to pass around CSV, BytesIO to write xlsx
#f = open("myfile.txt", "r", encoding="utf-8")

# prarse incoming csv into series of [operations]
#  - have is jst a series of buy
#  - a given year -- say 2020 -- can "have buy, sell, interest, lose"
#    + a "buy" seaches for right to store in [assest] -- built in OOP
#    + a sell remove bought item[s] from [asset] and makes an [event] line
#    + interset is an [event] and a "buy"
#    + lose is a "sell" for $0
#  - seperate long / short into a "buy and sell" for each line
# !! if excange is NULL, then use "COINBASE"
'''
in:
  - StringIO -- a CSV with a header -- file in memory
  - howto parse file into ops (header_style)
  
out:
  - a list of operations in JSON format
'''
def csv_to_operations(csv_stream, header_style): 
      
    # create a list
    if header_style == 1:
        data = []
    elif header_style == 2:
        data = []
    else:
        print('Error unknown input format')
        exit 0

    #without heder
    #reader = list(csv.reader(StringIO(csv_stream.getvalue()), lineterminator='\n'))
    #with header
    reader = list(csv.DictReader(StringIO(csv_stream.getvalue()), lineterminator='\n'))
    for row in reader:
        # TODO: -- logic here -- process [row] into one or more [operations]
        data.append(operations)

    # list of operations in JSON format
    return json.dumps(data)





# TODO: process operations into [assets] -- stuff held -- and in [event] log to report





# TODO: output reports to files




# TODO: save in db / recall from db -- only [assets]?, put in OOP?




if __name__ == "__main__":
    # execute only if run as a script -- is a test

    csv_have = "????"
    g = StringIO()
    for row in csv_have.splitlines():
        g.write(row)
        g.write("\n")
    print(csv_to_operations(g))
    #??? expectation ???
