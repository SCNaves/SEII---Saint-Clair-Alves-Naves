weigth = int(input('Digite o seu peso:'))
unit = input('K(g) ou L(b) ?')

if unit.upper() == "K":
    converted = weigth / 0.45
    input("Seu peso em libras e " + str(converted))
else:
    converted = weigth * 0.45
    input("Seu peso em kg e " + str(converted))
    