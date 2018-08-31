bitcoin = 9000
usdt = .99

if bitcoin<=8000 and usdt<=1:
    print("Bitcoin seems to be Stable. but You need To improvise")
elif bitcoin>=8001 and usdt<=1:
    print("You need to Sell Bitcoin and Buy USDT.")
elif bitcoin<=8000 and usdt >=1:
    print("You need to Buy Bitcoin using USDT.")
else:
    print("Check the programming code there must be a logical error.")