import random
from art import input_color
from regicide import draw_cards


def add_card(card, large_royal_played):
    current_value = card[0]
    if current_value == "Jes":
        current_value = 0
    if current_value == "A":
        current_value = 1
    elif current_value == "J":
        current_value = 10
    elif current_value == "Q":
        current_value = 15
        large_royal_played = True
    elif current_value == "K":
        current_value = 20
        large_royal_played = True
    return current_value, large_royal_played


def block_attack(current_baddie, hand, card, discard_pile):
    if len(hand) > 0:
        block, _ = add_card(card, False)
        current_baddie["this_attack"] -= block
        discard_pile.append(card)
        hand.remove(card)
        return current_baddie
    else:
        return "Game Over"


def attack_suit_parse(card, suits, current_baddie):
    if card[1] == input_color("♠", "BLACK", "WHITE") and current_baddie["Blocks"] != input_color("♠", "BLACK",
                                                                                                 "WHITE"):
        suits[3] = True
    elif card[1] == input_color("♥", "RED", "WHITE") and current_baddie["Blocks"] != input_color("♥", "BLACK",
                                                                                                 "WHITE"):
        suits[1] = True
    elif card[1] == input_color("♣", "BLACK", "WHITE") and current_baddie["Blocks"] != input_color("♣", "BLACK",
                                                                                                   "WHITE"):
        suits[0] = 2
    elif card[1] == input_color("♦", "RED", "WHITE") and current_baddie["Blocks"] != input_color("♦", "RED",
                                                                                                 "WHITE"):
        suits[2] = True
    return suits


def attack(draw_pile, current_baddie, hand, hands, discard_pile, *user_input):
    attack_value = 0
    previous_value = 0
    suits = [1, False, False, False]
    large_royal_played = False
    values = [card[0] for card in user_input]
    if len(values) > 2:
        if "A" in values:
            return input_color("Cannot play ace with combo", "RED")
        if not sum(values) / len(values) == values[0]:
            return input_color("Illegal pairing", "RED")
    for card in user_input:
        current_value, large_royal_played = add_card(card, large_royal_played)
        attack_value += current_value
        if ((attack_value > 11 and not large_royal_played) or
                (large_royal_played and not current_value <= 1 and not previous_value <= 1) or
                (current_value != previous_value and not current_value <= 1 and not previous_value <= 1)):
            return input_color("Illegal pairing", "RED")
        suits = attack_suit_parse(card, suits, current_baddie)
        previous_value = int(current_value)
    for card in user_input:
        hand.remove(card)
    if suits[2]:
        if not hands:
            draw_cards(draw_pile, hand, attack_value)
        else:
            draw_cards(draw_pile, hand, attack_value, 9 - len(hands), hands)
    if suits[1]:
        for number in range(attack_value):
            if len(discard_pile) > 0:
                drawn_card = random.choice(discard_pile)
                discard_pile.remove(drawn_card)
                draw_pile.insert(0, drawn_card)
    if suits[3]:
        current_baddie["this_attack"] -= attack_value
        current_baddie["damage"] -= attack_value
    for card in user_input:
        discard_pile.append(card)
    current_baddie["health"] -= (attack_value * suits[0])
    return current_baddie


