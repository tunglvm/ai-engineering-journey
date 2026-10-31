menu = {
    "Mojito": 90000,
    "Margarita": 120000,
    "Negroni": 150000,
    "Cuba Libre": 80000,
    "Gin Tonic": 95000
}

cheap_drinks = []

for name, price in menu.items():
    if price < 100000:
        cheap_drinks.append(name.upper())

print(cheap_drinks)

cheap_drinks = [name.upper() for name, price in menu.items() if price < 100000]