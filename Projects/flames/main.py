from operator import indexOf
from zoneinfo import reset_tzpath

word1 = "negoslav"
word2 = "vladislava"


def count_letters(word):
    letter_dict = {}
    for letter in word:
        if letter in letter_dict:
            letter_dict[letter] += 1
        else:
            letter_dict[letter] = 1
    return  letter_dict

word1_dict = count_letters(word1)
word2_dict = count_letters(word2)
print(word1_dict,word2_dict)

letter_list = []

for letter in word1_dict:
    if letter in word2_dict:
        if word1_dict[letter] > word2_dict[letter]:
            letter_list.extend(letter * (word1_dict[letter] - word2_dict[letter]))
        elif word1_dict[letter] == word2_dict[letter] :
             pass
    else:
        letter_list.extend(letter * word1_dict[letter])
for letter in word2_dict:
    if letter in word1_dict:
        if word2_dict[letter] > word1_dict[letter]:
            letter_list.extend(letter * (word2_dict[letter] - word1_dict[letter]))
        elif word2_dict[letter] == word1_dict[letter]:
            pass
    else:
        if word2_dict[letter] not in word1_dict:
            letter_list.extend(letter * word2_dict[letter])


print("Letter list - ",letter_list)

flames = ["Friends", "Love", "Affection", "Marriage", "Enemy", "Siblings"]

while len(flames) > 1:
        x = len(letter_list) % len(flames)
        flames.remove(flames[x-1])

print(flames)