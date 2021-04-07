from datetime import datetime


class assests():
    def __init__(self):
        # dict of list of dict
        # {asset:[{buy}, {buy, {buy}], ... }
        self.stuff = {}

    def buy(self,Date,Operation,Asset,Amount,Price,Exchange):
        transaction = {"date_bought": Date, "amount_bought": Amount, "price_bought": Price, "exchange_bought": Exchange}
        if Asset in self.stuff:
            # asset exists -- sort by purchase date to make FIFO
            buy_list = self.stuff[Asset]
            index = 0
            inserted = False
            for item in buy_list:
                if Date < item.date_bought:
                    index += 1
                else:
                    buy_list.insert(transaction, index)
                    inserted = True
            # if never <, then transaction is earliest
            if not inserted:
                buy_list.insert(transaction, 0)
                
            # save updated list with new transaction
            self.stuff[Asset] = buy_list
    else:
        # first asset of that type
        self.stuff[Asset] = []
        self.stuff[Asset].append(transaction)

    def sell(self,Date,Operation,Asset,Amount,Price,Exchange):
        event = {"date_sold": Date, "amount_sold": Amount, "price_sold": Price, "exchange_sold": Exchange}
        if Asset in self.stuff:
            # TODO: founnd it
        else:
            print("Error trying to sell non-existant asset " + Asset + ":")
            print("  " + event)

    # TODO: load/store to ineract with db through models
