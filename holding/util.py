import csv, json
from collections import OrderedDict

from io import StringIO, BytesIO
# StringIO to pass around CSV, BytesIO to write xlsx
#f = open("myfile.txt", "r", encoding="utf-8")

from openpyxl import Workbook

# upload xlsx and split into 3 csv

# upload CSV and open (pass csv_have, csv_short=None, csv_long=None)
#    json_have = make_json(csv_have, None)
#    json_temp = make_json(csv_short, None)
#    json_sell = make_json(csv_short, json_temp)

# file object (BytesIO) of CSV with headers to JSON string to be stored -- import/ uses this JSON or POST as a record of holdings
def make_json(csv_stream, json_string): 
      
    # create a dictionary 
    if json_string == None:
        data = []
    else:
        data = json_string

    #without heder
    #reader = list(csv.reader(StringIO(csv_stream.getvalue()), lineterminator='\n'))
    #with header
    reader = list(csv.DictReader(StringIO(csv_stream.getvalue()), lineterminator='\n'))
    for row in reader:
        data.append(row)

    return json.dumps(data)

# tansactions (json.dumps(CSV) into BUY/SELL orders to be processed)



##### returns JSON objects for processing

if __name__ == "__main__":
    # execute only if run as a script
    csv_have = "fruit,amount\napple,1\npeach,2"
    print(csv_have)
    print()
    g = StringIO()
    for row in csv_have.splitlines():
        g.write(row)
        g.write("\n")
    print(make_json(g, None))
