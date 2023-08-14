temperature = int(input('Digite a temperatura atual:' ))

if temperature < 10:
    print('Vista um casaco')
elif temperature > 20 and temperature <= 29:
    print('O clima esta bom, aproveite uma praia')
elif temperature >= 30:
    print('Ligue o ar condicionado')
    