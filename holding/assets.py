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
        # tax is a list of dict -- not the BUY, only stuff to report to IRS
        self.tax = []

    def buy(self,Date,Asset,Amount,Price,Exchange):
        transaction = {"date_bought": Date, "amount_bought": Amount, "price_bought": Price, "exchange_bought": Exchange}
        if Asset in self.stuff:
            # asset exists
            buy_list = self.stuff[Asset]
            index = 0
            for item in buy_list:
                # sort -- currently newest, mean for oldest fist -- FIFO!!!!
                # find index
                 if Date < item["date_bought"]:
                    # incoming earlier, insert before here
                     break
                 elif Date > item["date_bought"]:
                    # incoming date later -- keep gwalking
                    index += 1
            # insert once
            buy_list.insert(index, transaction)
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
        if Asset in self.stuff:
            # found asset
            bought_list = self.stuff[Asset]
            total = Amount
            for item in bought_list:
                if total >= float(item["amount_bought"]):
                    # item needs to be removed totally & update [event]
                    total -= float(item["amount_bought"])
                    self.stuff[Asset].pop(0)

                    new_price = (Price / Amount) * float(item["amount_bought"])

                    # deepcopy for use only in [events] not in [assets]
                    t2 = deepcopy(item)
                    t2.update({"date_sold": Date, "exchange_sold": Exchange})
                    t2.update({"asset": Asset, "action": "SELL"})
                    t2.update({"amount_sold": item["amount_bought"], "price_sold": new_price})
                    t2.update({"term": "short"}) # TODO -- be more agreesive about short vs long
                    self.event.append(t2)
                    self.tax.append(t2)

                else:
                    # item just needs adjusting & update [event]
                    old_price = item["price_bought"]
                    old_amount = item["amount_bought"]
                    
                    new_amount = float(old_amount) - total
                    new_price = (float(old_price) / float(old_amount)) * new_amount
                    
                    total_sold = total
                    total_price = (float(old_price) / float(old_amount)) * total_sold
                    total = 0
                    
                    # update item in original [asset] at HEAD of list
                    self.stuff[Asset][0]["price_bought"] = new_price
                    self.stuff[Asset][0]["amount_bought"] = new_amount
                    
                    # deepcopy for use only in [events] not in [assets]
                    t2 = deepcopy(item)
                    t2.update({"date_sold": Date, "exchange_sold": Exchange})
                    t2.update({"asset": Asset, "action": "SELL"})
                    t2.update({"amount_sold": total_sold, "price_sold": total_price})
                    t2.update({"term": "short"}) # TODO -- be more agreesive about short vs long
                    self.event.append(t2)
                    self.tax.append(t2)

                if total == 0:
                    break

            if total < 0:
                print("Error -- more to be sold than have")
                exit(0)
        else:
            print("Error trying to sell non-existant asset " + Asset + ":")
            print("  " + event)

    def interest(self,Date,Asset,Amount,Price,Exchange):
                    t2 = {}
                    t2.update({"date_sold": Date, "exchange_bought": Exchange})
                    t2.update({"asset": Asset, "action": "INTEREST"})
                    t2.update({"amount_sold": Amount, "price_sold": Price})
                    t2.update({"term": "short"}) # all interest is short term
                    self.event.append(t2)
                    self.tax.append(t2)

    # ops -- excute from HAVE/BUY/SELL/INTEREST/LOSE &  AIRDROP (like INTEREST but diiferent [assest] to BUY)
    def operands(self,Operation,Date,Asset,Amount,Price,Exchange):
        if Operation == "HAVE" or Operation == "BUY":
            self.buy(Date,Asset,Amount,Price,Exchange)
        elif Operation == "INTEREST":
            self.interest(Date,Asset,Amount,Price,Exchange)
            self.buy(Date,Asset,Amount,Price,Exchange)
        elif Operation == "SELL":
            self.sell(Date,Asset,Amount,Price,Exchange)
        elif Operation == "LOSE":
            self.sell(Date,Asset,Amount,0.0,Exchange)
        else:
            print("Unknown Operation: " + Operation)
            exit(0)

    # TODO: load/store to ineract with db through models -- .save()
