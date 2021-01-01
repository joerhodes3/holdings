import csv, json

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
        data = {}
    else:
        data = json_string

    lines = csv_stream.getvalue()
    print(lines)

    reader = csv.reader(csv_stream)
    print(reader)
    next(reader) # skip header
    data = []
    for row in reader:
        data.append(row)

    print(data)
  
    ###return json.dumps(csv_dict)

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
