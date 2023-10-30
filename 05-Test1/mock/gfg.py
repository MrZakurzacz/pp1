import random as ran

#a
a = ran.randint(0,1)

#b

counter = 0
used_numbers = []
total = 0
cards_dict = {
    1: 'Ace of Hearts', 2: '2 of Hearts', 3: '3 of Hearts', 4: '4 of Hearts',
    5: '5 of Hearts', 6: '6 of Hearts', 7: '7 of Hearts', 8: '8 of Hearts',
    9: '9 of Hearts', 10: '10 of Hearts', 11: 'Jack of Hearts',
    12: 'Queen of Hearts', 13: 'King of Hearts',

    14: 'Ace of Diamonds', 15: '2 of Diamonds', 16: '3 of Diamonds', 17: '4 of Diamonds',
    18: '5 of Diamonds', 19: '6 of Diamonds', 20: '7 of Diamonds', 21: '8 of Diamonds',
    22: '9 of Diamonds', 23: '10 of Diamonds', 24: 'Jack of Diamonds',
    25: 'Queen of Diamonds', 26: 'King of Diamonds',

    27: 'Ace of Clubs', 28: '2 of Clubs', 29: '3 of Clubs', 30: '4 of Clubs',
    31: '5 of Clubs', 32: '6 of Clubs', 33: '7 of Clubs', 34: '8 of Clubs',
    35: '9 of Clubs', 36: '10 of Clubs', 37: 'Jack of Clubs',
    38: 'Queen of Clubs', 39: 'King of Clubs',

    40: 'Ace of Spades', 41: '2 of Spades', 42: '3 of Spades', 43: '4 of Spades',
    44: '5 of Spades', 45: '6 of Spades', 46: '7 of Spades', 47: '8 of Spades',
    48: '9 of Spades', 49: '10 of Spades', 50: 'Jack of Spades',
    51: 'Queen of Spades', 52: 'King of Spades'
}
b = ran.randint(1,52)
clubs_range = range(27, 39)
def club():
    for i in range(3):
        card_number = ran.randint(1,52)
        while card_number in used_numbers:
            card_number = ran.randint(1,52)
        used_numbers.append(card_number)
        if card_number in clubs_range:
            counter+=1
    return counter

club()