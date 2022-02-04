#   weird game with cards
import random


def deal_card():
    """Returns random card from the deck of cards"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card


def calculate_score(cards):
    return sum(cards)


def compare(user_score, computer_score):
    if user_score == computer_score:
        return "Draw"
    elif computer_score == 0:
        return "Lost Opponent has the blackjack"
    elif user_score == 0:
        return "Won with a blackjack"
    elif user_score > 21:
        return "You went over, You lose"
    elif computer_score > 21:
        return "Opponent went over, You won"
    elif user_score > computer_score:
        return "You won"
    else:
        return "You lose"


user_cards = []
computer_cards = []
is_game_over = False

for _ in range(2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())

while not is_game_over:
    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)
    print(f" Your cards: {user_cards} and Your Score: {user_score}")
    print(f" Computer's first card: {computer_cards[0]} ")

    if user_score == 0 or computer_score == 0 or user_score > 21:
        is_game_over = True
    else:
        user_should_deal = input("Type 'Y' to continue and 'N' to quit: ").upper()
        if user_should_deal == "Y":
            user_cards.append(deal_card())
        else:
            is_game_over = True

while computer_score != 0 and computer_score < 17:
    computer_cards.append(deal_card())
    computer_score = calculate_score(computer_cards)
print(f" Your final card is : {user_cards} and final score is : {user_score}")
print(f" Computer's final card is : {computer_cards} and computer's score is : {computer_score}")
print(compare(user_score, computer_score))


def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 0:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)

        return sum(cards)
