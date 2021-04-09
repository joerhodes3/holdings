from datetime import date
from copy import deepcopy

#from models import ....


class asset_items():
    def __init__(self):
        # dict of list of dict
        # {asset:[{buy}, {buy, {buy}], ... }
        self.stuff = {}
        # event is a list of dict -- one or more things happened
        self.event = []

    def buy(self,Date,Asset,Amount,Price,Exchange):
        transaction = {"date_bought": Date, "amount_bought": Amount, "price_bought": Price, "exchange_bought": Exchange}
        if Asset in self.stuff:
            # asset exists -- sort by purchase date to make FIFO
            buy_list = self.stuff[Asset]
            index = 0
            inserted = False
            for item in buy_list:
                if Date < item["date_bought"]:
                    index += 1
                else:
                    self.stuff[Asset].insert(index, transaction)
                    inserted = True
                    break
            # if never <, then transaction is earliest
            if not inserted:
                self.stuff[Asset].insert(0, transaction)

            # save updated list with new transaction
            self.stuff[Asset] = buy_list
        else:
            # first asset of that type
            self.stuff[Asset] = []
            self.stuff[Asset].append(transaction)
    
        t2 = deepcopy(transaction)
        t2.update({"asset": Asset, "action": "BUY"})
        self.event.append(t2)

    def sell(self,Date,Asset,Amount,Price,Exchange):
        event = []
        event.append({"date_sold": Date, "exchange_sold": Exchange})
        price_per_item_sold = Price / Amount
        if Asset in self.stuff:
            # found asset
            bought_list = self.stuff[Asset]
            event_index = 0
            total = Amount
            for item in bought_list:
                if total >= float(item["amount_bought"]):
                    # item needs to be removed totally & update [event]
                    total -= float(item["amount_bought"])
                    self.stuff[Asset].pop(0)

                    new_price = price_per_item_sold * float(item["amount_bought"])
                    item.update({"asset": Asset, "action": "SELL"})
                    item.update({"amount_sold": item["amount_bought"], "price_sold": new_price})
                    item.update({"term": "short"})
                    event[event_index].update(item)
                    event_index += 1
                    if total != 0:
                        # not Done, prepare next event
                        event.append({"date_sold": Date, "exchange_sold": Exchange})
                else:
                    # item just needs adjusting & update [event]
                    old_price = float(self.stuff[Asset]["price_bought"])
                    old_amount = float(self.stuff[Asset]["amount_bought"])
                    new_amount = old_amount - total
                    new_price = (old_price / old_amount) * new_amount
                    total_sold = total
                    total_price = (old_price / old_amount) * total_sold
                    total = 0
                    self.stuff[Asset]["price_bought"] = new_price
                    self.stuff[Asset]["amount_bought"] = new_amount

                    item.update({"asset": Asset, "action": "SELL"})
                    item.update({"amount_sold": total_sold, "price_sold": price_sold})
                    item.update({"term": "short"})
                    event[event_index].update(item)
                    event_index += 1

                    self.event.append(event)

                if total == 0:
                    break

            if total < 0:
                print("Error -- more to be sold than have")
                exit(0)
        else:
            print("Error trying to sell non-existant asset " + Asset + ":")
            print("  " + event)

    # ops -- excute from HAVE/BUY/SELL/INTEREST/LOSE
    def operands(self,Operation,Date,Asset,Amount,Price,Exchange):
        print("  DEBUG: Operation: "+ Operation)
        if Operation == "HAVE" or Operation == "BUY":
            print("  DEBUG: BUY")
            self.buy(Date,Asset,Amount,Price,Exchange)
        elif Operation == "INTEREST":
            print("  DEBUG: INTEREST")
            #TODO: update event
            self.buy(Date,Asset,Amount,Price,Exchange)
        elif Operation == "SELL":
            print("  DEBUG: SELL")
            self.sell(Date,Asset,Amount,Price,Exchange)
        elif Operation == "LOSE":
            self.sell(Date,Asset,Amount,0.0,Exchange)
        else:
            print("Unknown Operation: " + Operation)
            exit(0)

    # TODO: load/store to ineract with db through models -- .save()
