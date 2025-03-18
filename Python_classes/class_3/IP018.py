n = int(input())
total_price = 0.0

for i in range(1, n + 1):
    night_price = 50/i
    total_price = total_price + night_price
    print(f"Night {i}: {round(night_price, ndigits=2)}E") 
print(f"Total: {round(total_price, ndigits=2)}E")
