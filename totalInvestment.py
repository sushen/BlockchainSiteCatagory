
total_investment = 0

#Grab hole data from coinmarketcap
Coins = {'Bitcoin' :7254.18, 'Ethereum':292.88 ,'XRP':0.340238, 'Bitcoin Cash':635.71 }

#Make a gui selector for which coin I invest
invested_coins = ['Bitcoin','Bitcoin Cash']

for invested_coin, price in Coins.items():
    if invested_coin in invested_coins:
        total_investment +=price


print("My total investment Coin Market price is {}".format(total_investment))

# Count Profite :
# My buing Price - Present Coin Market Price


