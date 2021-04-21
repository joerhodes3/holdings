import csv, json
from io import StringIO, BytesIO
from datetime import date
from copy import deepcopy

from assets import asset_items


# TEMP: global
things = asset_items()

# StringIO to pass around CSV, BytesIO to write xlsx
#f = open("myfile.txt", "r", encoding="utf-8")

# prarse incoming csv into series of [operations]
#  - have is just a series of buy
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
  - assests, events in JSON format [str, str]
'''
def csv_to_events(csv_stream, header_style):
    if header_style == "have":
        #with header -- Date,Operation,Asset,Amount,Price,Exchange
        csv_reader = list(csv.DictReader(StringIO(csv_stream.getvalue()), lineterminator='\n'))
        reader = deepcopy(csv_reader)
        for row in reader:
            # prescreen incoming csv to make sure only legal Operations 
            if not(row["Operation"] == "HAVE"):
                print("Bad opperand")
                exit(0)
        reader = deepcopy(csv_reader)
        for row in reader:
            # go through and procees all Operations as BUY
            temp_date_object = row["Date"] ###date(row["Date"])
            things.operands(row["Operation"],temp_date_object,row["Asset"],row["Amount"],row["Price"],row["Exchange"])
        # dump out all BUY events in JSON
        return json.dumps(things.stuff, indent=2, sort_keys=True),json.dumps(things.event, indent=2, sort_keys=True)
        # TODO: save() to db
    elif header_style == "year":
        # with header -- Date,Operation,Asset,Amount,Price,Exchange
        csv_reader = list(csv.DictReader(StringIO(csv_stream.getvalue()), lineterminator='\n'))
        reader = deepcopy(csv_reader)
        for row in reader:
            # prescreen incoming csv to make sure only legal Operations 
            if not(row["Operation"] == "BUY" or row["Operation"] == "SELL" or row["Operation"] == "INTEREST"):
                print("Bad opperand for row" + str(row))
                exit(0)
        reader = deepcopy(csv_reader)
        for row in reader:
            # go through each row in have csv and procees as BUY/SELL/INEREST
            temp_date_object = ()
            try:
                temp_date_object = row["Date"] ###date(row["Date"])
            except:
                print("  DEBUG -- fail to get Date for "+str(row.__dict__))
            things.operands(row["Operation"],temp_date_object,row["Asset"],float(row["Amount"]),float(row["Price"]),row["Exchange"])
        # dump out all BUY events in JSON
        return json.dumps(things.stuff, indent=2, sort_keys=True),json.dumps(things.event, indent=2, sort_keys=True)
        # TODO: save() to db
    elif header_type == "long":
        # expect odd format and unwind into buy/sell events
        pass
    elif header_type == "short":
        # expect odd format and unwind into buy/sell events
        pass
    else:
        print('Error unknown input format')
        exit(0)




# TODO: process operations into [assets] -- stuff held -- and in [event] log to report





# TODO: output reports to files




# TODO: save in db / recall from db -- only [assets]?, put in OOP?




if __name__ == "__main__":
    # execute only if run as a script -- is like a test

    csv_have = open("csv/have.csv", mode="r", encoding="utf-8-sig")
    g = StringIO()
    for row in csv_have.readlines():
        row.strip()
        g.write(row)
        g.write("\n")
    csv_have.close()
    assets,events = csv_to_events(g, "have")
    ###print("--------assests---------"+assets+"-----events------"+events)
    #expectation
    things.event = [] # TEMP reset of events, so I just see year
    print("=================")
    print("   year")
    print("=================")
    csv_have = open("csv/2020.txt", mode="r", encoding="utf-8-sig")
    g = StringIO()
    for row in csv_have.readlines():
        row.strip()
        g.write(row)
        g.write("\n")
    csv_have.close()
    assets,events = csv_to_events(g, "year")
    ###print("--------assests---------"+assets+"-----events------"+events)
    print(events)
