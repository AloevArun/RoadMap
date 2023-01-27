words = [(str(input())), str(input()), str(input())]
words_length = []
for word in words:
    words_length.append(len(word))
words_length = sorted(words_length)
if words_length[2] - words_length[1] == words_length[1] - words_length[0] and words_length[1] > words_length[0]:
    print('YES')
else:
    print('NO')