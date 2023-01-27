n = str(input())
if len(n) != 5:
    rev_1 = n[::-1]
    rev_2 = rev_1[:5]
    rev_3 = n[0]
    rev_last = rev_3 + rev_2
    print(int(rev_last))
else:
    print(int(n[::-1]))

'''
s = input()
print(int(s[:-5] + s[-5:][::-1]))
'''