text = str(input())
cost = len(text) * 60
r_cost = cost // 100
k_cost = cost % 100
print(f'{r_cost} р. {k_cost} коп.')