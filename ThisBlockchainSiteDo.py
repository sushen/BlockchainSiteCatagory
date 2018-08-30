import webbrowser

#coinmarketcap.com, hitbtc.com, localbitcoins.com, sushenbiswas.com

website = 'sushenbiswas.com'

if website == 'coinmarketcap.com':
    webbrowser.open('http://coinmarketcap.com')
    print("Coinmarketcap Give you a preview of Crypto currency Market.")

elif website == 'hitbtc.com':
    webbrowser.open('http://hitbtc.com')
    print("hitbtc is a crypto currency exchange site.")

elif website == 'localbitcoins.com':
    webbrowser.open('http://localbitcoins.com')
    print("localbitcoins is a crypto currency buy/sell site.")

elif website == 'sushenbiswas.com':
    webbrowser.open('http://sushenbiswas.com')
    print("sushenbiswas is a crypto currency Tutorial site.")

else:
    print(" You type Some thing Wrong!")