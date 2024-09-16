"""Vow3l Count"""

from unidecode import unidecode

print()
print('Vow3l Count')
print()

phrase = input ('3nter a Word or Phase to Count Th3 Vow3ls: ')

final_phrase = unidecode(phrase)

Vow3ls = 0

for caractere in final_phrase:
    x = caractere
    if x == "a" or x == "e" or x == "i" or x == "o" or x == "u" or x == "A" or x == "E" or x == "I" or x == "O" or x == "U":
        Vow3ls += 1

print()
print('Your Phrase has <<<', Vow3ls, '>>> Vow3ls.')
print()
