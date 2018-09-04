Criptos = [('Bitcoin',.07), ('Ethereum',.09),( 'XRP',.15), ('Bitcoin Cash',.01), ('EOS',.06), ('Stellar',.02),('Litecoin',.06), ('Tether',.01)]

parcintage = 0
NewCripto = []

for cripto_name, cripto_percantige in Criptos:
    if parcintage >= .2:
        print("We rich the selling Precentige.")
        break

    else:
        print("Now Counting {} and it rech {}".format(cripto_name,cripto_percantige))
        NewCripto.append(cripto_name)
        parcintage += cripto_percantige

print("\nTotal Parcentage Rech {}".format(parcintage))
print("Cripto We Got for selling: {}".format(NewCripto))

print("\n \nNew Method: \n")

parcintage = 0
NewCripto = []

for cripto_name, cripto_percantige in Criptos:
    if parcintage >= .2:
        print("We rich the selling Precentige.")
        break

    elif parcintage + cripto_percantige >.2:
        print("{} may be bubble Item skip this pumping its rech {} ".format(cripto_name,cripto_percantige))
        continue

    else:
        print("Now Counting {} and it rech {}".format(cripto_name,cripto_percantige))
        NewCripto.append(cripto_name)
        parcintage += cripto_percantige

print("\nTotal Parcentage Rech {}".format(parcintage))
print("Cripto We Got for selling: {}".format(NewCripto))