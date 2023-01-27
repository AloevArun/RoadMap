price = int(input())
coin_counter = 0
while True:
    if price >= 25:
        coin_counter += 1
        price -= 25
    elif price >= 10:
        coin_counter += 1
        price -= 10
    elif price >= 5:
        coin_counter += 1
        price -= 5
    else:
        coin_counter += price
        break
print(coin_counter)