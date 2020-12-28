from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

#GET
@app.route('/about/')
def about():
    # is for tracking assets held (crypto works just like security -- intertest/staking proceed taxed as they accue, and then are cost basis)
    return 'Hello, World!'

##########################
# a HAVE object is:
#   [symbol, date_bought, total_price_bought, quantity_bought]
# a SELL (short/long) is:
#   [symbol, date_bought, total_price_bought, date_sold, total_price_sold, quantity_sold]
##########################
#GET
@app.route('/clear/')
def drop():
    #empty short,long,have
    return 'Hello, World!'

#POST
@app.route('/import/<string:input_format>')
def input(input_format):
    # NOTE: import is a python keyword, so funtion is named input
    if input_format == 'CSV':
        #no prior short/long
        return 'CSV [upload file]'
    elif input_format == 'XLSX':
        #in addition to HAVE[] get previous short/long
        return 'Excel [upload file]'
    elif input_format == 'JSON':
        return 'JSON passed as data in POST'
    else:
        return 'unknown format, I only know howto parse: CSV,XLSX,JSON'

#POST
@app.route('/adjust/<string:action>')
def adjust(action):
    # TODO: GIVE / GET as gift -- payment
    if action == 'BUY':
        #updates HAVE[]
        return 'Buy [symbol, date, price, quantity]'
    elif action == 'SELL':
        #HAVE[symbol] sorted by date
        #remove oldest from HAVE[] until quantity_to_sell is 0
        #   if SELL[amount] < HAVE[amount] -- HAVE[amount] = HAVE[amount] - SELL[amount]),
        #   else remove all of entry and try next with SELL[amount] =- HAVE[quantity]
        #create INCOME[] entries (append to either short/long) 
        return 'Sell [symbol, date, price, quantity]'
    elif action == 'LOSE':
        # just like SELL, but no INCOME[] -- short or long
        return 'Lose [symbol, date, price, quantity]'
    elif action == 'SHOW':
        return 'Show'
    else:
        return 'unknown action, I only know howto: BUY,SELL,LOSE,SHOW'

#GET -or- GraphQL
@app.route('/analyze/')
def analyze():
    # total amount invested (and current value = amount * current price),
    #    current price is gotten based on known types (cryptos, stocks, ...)
    # income is sum of short/long[total_price_sold]
    # pie chart -- % of investment
    return 'Hello, World!'

#GET
@app.route('/output/')
def output():
    # 3 sheets (short, long, assesets_remaining)
    return 'Hello, World!'
