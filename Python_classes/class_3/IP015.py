price = float(input())
customer = input()

if customer == "F":
    if price > 200:
        price = price * 0.90
        print(f"Customer: {customer} | Price: {round(price, ndigits=3)}")
    elif price <= 200 and price >= 50:
        price = price * 0.95
        print(f"Customer: {customer} | Price: {round(price, ndigits=3)}")
    elif price < 50 and price >=1:
        price = price * 0.98
        print(f"Customer: {customer} | Price: {round(price, ndigits=3)}")

if customer == "P":
    price = price * 1.06
    print(f"Customer: {customer} | Price: {round(price, ndigits=3)}")