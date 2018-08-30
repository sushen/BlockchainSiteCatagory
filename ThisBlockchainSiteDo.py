import webbrowser
import ctypes

#coinmarketcap.com, hitbtc.com, localbitcoins.com, sushenbiswas.com

website = ''

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
    print("SushenBiswas is a crypto currency Tutorial site.")

else:
    def Mbox(title, text, style):
        return ctypes.windll.user32.MessageBoxW(0, text, title, style)
    Mbox('Attention', 'You type Some thing Wrong! \nYou need to enter commented site to learn Crypto currency. \nThose are coinmarketcap.com, hitbtc.com, localbitcoins.com, sushenbiswas.com', 1)
