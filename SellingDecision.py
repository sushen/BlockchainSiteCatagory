bitcoin = 12000
sellingDecision = None


if bitcoin <=5000:
    sellingDecision = "Buy Bitcoin"

elif 5000 <= bitcoin <=7000:
    sellingDecision = "Buy Lower price Alter coin"

elif 7000 <= bitcoin <= 11000:
    sellingDecision = "Sell Bitcoin"


if sellingDecision:
    Decision = "You Decision have to {}".format(sellingDecision)
else:
    Decision = "Now Price is more than 11000. Decide!"


print(Decision)