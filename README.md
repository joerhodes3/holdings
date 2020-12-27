# holdings

# about/ -- is for tracking assets held (crypto works just like security -- intertest/staking proceed taxed as they accue, and then are cost basis)

# convert csv -or xls- to JSON  object to be POSTed
- csv -> python dict -> json.dumps()
    * define python dict as a series of key/value foreach line in
- ALSO, make trasaction to JSON

# use Flask to make following ReST API, passes JSON to javascipt/VUE [with router]
- clear (delete everything HAVE, SELL, and INCOME) [GET]
- import (load previous csv cost basis) [POST csv as JSON object?]
    + buy / sell [these operations are POST endpoints]
        * buy -- inserts item into HAVE[]
        * give (buy + INCOME[])
        * sell - HAVE is ordered by date,
          loop through HAVE amounts until sell amount met (remove from HAVE / make SELL entry -- if SELL[amount] < HAVE[amount] -- HAVE[amount] = HAVE[amount] - SELL[amount]),
          also adjust HAVE[cost] 
        * loose -- (recocile -- like a sell that only update HAVE[]), ?LOOSE[]?
- output (2 workbooks) [GET]
    * simple current open positions -- to import
    * 3 sheets (short, long, income)
- analyze [GET]
    * total amount invested (and current value = amount * current price),
      current price is gotten based on known types (cryptos, stocks, ...)
    * pie chart -- % of investment

# manually reconsile until have loose()-- is likely LTC on some other exchange
