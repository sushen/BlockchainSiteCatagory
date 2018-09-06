CriptoNames = input("Type your Cripto Name : ").title().split(",")
BuyingPricess = input("What Price You pay to buy : ").split(",")
HowMuchs = input("How Much you buy : ").split(",")

massage = "your {},is a mesurable criptocurrency \n and you buying price was {},\n it is too high price for buying and you buy it {},\n next week it my be sell in  {}. "

for CriptoName, BuyingPrice, HowMuch in zip(CriptoNames, BuyingPricess, HowMuchs):
    print(massage.format(CriptoName, BuyingPrice, HowMuch, int(BuyingPrice) + int(BuyingPrice)/2))