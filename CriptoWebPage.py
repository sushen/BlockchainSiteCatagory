topCripto = ['Bitcoin', 'Ethereum', 'XRP', 'Bitcoin Cash', 'EOS', 'Stellar','Litecoin', 'Tether']

webpage = "<head>\n"


for cripto in topCripto:
    webpage += "<menu>{}</menu> \n".format(cripto)

webpage += "</head>"

print(webpage)