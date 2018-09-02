topCripto = ['Bitcoin', 'Ethereum', 'XRP', 'Bitcoin Cash', 'EOS', 'Stellar','Litecoin', 'Tether']

uppercase_Cripto = []
lowercase_cripto = []
topCriptoIndex = []

for Cripto in topCripto:
    uppercase_Cripto.append(Cripto.upper())
    lowercase_cripto.append(Cripto.lower())

for Cripto_Index in range(len(topCripto)):
    topCriptoIndex.append(Cripto_Index)

for money in range(len(topCripto)):
    topCripto[money] = topCripto[money]

print(lowercase_cripto)
print(uppercase_Cripto)
print(topCriptoIndex)


print(topCripto)