counter = 0
while True:
    text = input()
    if text not in ('стоп', 'хватит', 'достаточно'):
        counter += 1
    else:
        print(counter)
        break
