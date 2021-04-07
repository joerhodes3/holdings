from datetime import date


class assests():
    def __init__(self):
        # dict of list of dict
        # {asset:[{buy}, {buy, {buy}], ... }
        self.stuff = {}
        # event is a list of dict -- one or more things happened
        event = []

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

    transaction.extend({"asset": Asset, "action": "BUY"})
    self.event.append(transation)

    def sell(self,Date,Operation,Asset,Amount,Price,Exchange):
        # event is a list of dict -- one or more
        event = []
        event.append({"date_sold": Date, "amount_sold": Amount, "price_sold": Price, "exchange_sold": Exchange})
        if Asset in self.stuff:
            # founnd asset
            bought_list = self.stuff[Asset]
            event_index = 0
            total = Amount
            for item in bought_list and total != 0:
                if total >= item.amount_bought:
                    # item needs to be removed totally !! & update [event] !!
                else:
                    # item just needs adjusting !! & update [event] !!
            if total != 0:
                print("Error -- more to be sold than have")
       else:
            print("Error trying to sell non-existant asset " + Asset + ":")
            print("  " + event)

    # TODO: load/store to ineract with db through models -- .save()
