import random
import os
import sys

HELPTEXT = (
    "\n\nThis is a single player adaptation of the board/ card game Regicide."
    "\n\n    To use a combo or an animal companion in the game:"
    "\n\t1.) Type the index of each card and press enter"
    "\n\t    (For instance if you want to play the 0th card and the 5th card type 05 or 50 and press enter, this will play both cards)"
    "\n\t2.) Cards of the same type can be played together as long as the total value doesn't exceed 10 for instance you can play 4 twos or 2 fives"
    "\n\t3.) You can play an ace paired with any other card"
    "\n\t4.) If you play multiple cards the effects of each card will be applied"
    "\n\n\tIf for whatever reason you ever want to yield, type 8."
    "\n\tTo use a Jester type 9."
    "\n\n    See the rest of the rules for the game at regicide's website:"
    "\n\tregicidegame.com\n")


def input_color(input_string: str, color: str, bg_color="") -> str:
    """
    Inserts text color and optionally a background color into a string.

    :param input_string: a string
    :param color: an all caps string defining and limited to the terminal text color options
    :param bg_color: an all caps string limited to the terminal background color options
    :precondition: three strings
    :return: a string with the correct text color and background color
    """
    if color == "BLACK":
        color = "\033[30m"
    elif color == "RED":
        color = '\033[31m'
    elif color == "GREEN":
        color = '\033[32m'
    elif color == "YELLOW":
        color = '\033[33m'
    elif color == "BLUE":
        color = '\033[34m'
    elif color == "MAGENTA":
        color = '\033[35m'
    elif color == "CYAN":
        color = '\033[36m'
    elif color == "LIGHT_GRAY":
        color = '\033[37m'
    elif color == "DARK_GRAY":
        color = '\033[90m'
    elif color == "BRIGHT_RED":
        color = '\033[91m'
    elif color == "BRIGHT_GREEN":
        color = '\033[92m'
    elif color == "BRIGHT_YELLOW":
        color = '\033[93m'
    elif color == "BRIGHT_BLUE":
        color = '\033[94m'
    elif color == "BRIGHT_MAGENTA":
        color = '\033[95m'
    elif color == "BRIGHT_CYAN":
        color = '\033[96m'
    elif color == "WHITE":
        color = '\033[97m'
    if bg_color == "BLACK":
        bg_color = '\033[40m'
    elif bg_color == "RED":
        bg_color = '\033[41m'
    elif bg_color == "GREEN":
        bg_color = '\033[42m'
    elif bg_color == "YELLOW":
        bg_color = '\033[43m'  # orange on some systems
    elif bg_color == "BLUE":
        bg_color = '\033[44m'
    elif bg_color == "MAGENTA":
        bg_color = '\033[45m'
    elif bg_color == "CYAN":
        bg_color = '\033[46m'
    elif bg_color == "DARK_GRAY":
        bg_color = '\033[100m'
    elif bg_color == "BRIGHT_RED":
        bg_color = '\033[101m'
    elif bg_color == "BRIGHT_GREEN":
        bg_color = '\033[102m'
    elif bg_color == "BRIGHT_YELLOW":
        bg_color = '\033[103m'
    elif bg_color == "BRIGHT_BLUE":
        bg_color = '\033[104m'
    elif bg_color == "BRIGHT_MAGENTA":
        bg_color = '\033[105m'
    elif bg_color == "BRIGHT_CYAN":
        bg_color = '\033[106m'
    elif bg_color == "WHITE":
        bg_color = '\033[107m'
    return f"{color}{bg_color}{input_string}\033[0m"


def new_deck():
    """
    Creates a new deck of cards containing each card from ace through 10

    :postcondition: a list
    :return: the list of cards from ace through ten
    """
    deck = []
    for number in range(1, 11):
        for suit in [input_color("♠", "BLACK", "WHITE"), input_color("♥", "RED", "WHITE"),
                     input_color("♣", "BLACK", "WHITE"), input_color("♦", "RED", "WHITE")]:
            if number == 1:
                deck.append(("A", suit))
            else:
                deck.append((number, suit))
    return deck


def enemies():
    """
    Randomizes the pile of enemies with kings at the bottom and Jacks on the top

    :return: the pile of enemies kins at bottom queens in middle and jacks on the top with their suits disorganized
    """
    enemy_list = []
    suits = [input_color("♠", "BLACK", "WHITE"), input_color("♥", "RED", "WHITE"), input_color("♣", "BLACK", "WHITE"),
             input_color("♦", "RED", "WHITE")]
    for royal in ["K", "Q", "J"]:
        random.shuffle(suits)
        for suit in suits:
            enemy_list.append((str(royal), suit))
    return enemy_list


def suit_interpreter(suit_symbol, letter):
    if suit_symbol == input_color("♠", "BLACK", "WHITE"):
        return f"{input_color(" Spades ", "BLACK", "WHITE")} {input_color(letter, "BLACK", "WHITE")}{input_color("♠", "BLACK", "WHITE")}"
    elif suit_symbol == input_color("♥", "RED", "WHITE"):
        return f"{input_color(" Hearts ", "RED", "WHITE")} {input_color(letter, "BLACK", "WHITE")}{input_color("♥", "RED", "WHITE")}"
    elif suit_symbol == input_color("♣", "BLACK", "WHITE"):
        return f"{input_color(" Clubs ", "BLACK", "WHITE")} {input_color(letter, "BLACK", "WHITE")}{input_color("♣", "BLACK", "WHITE")}"
    elif suit_symbol == input_color("♦", "RED", "WHITE"):
        return f"{input_color(" Diamonds ", "RED", "WHITE")} {input_color(letter, "BLACK", "WHITE")}{input_color("♦", "RED", "WHITE")}"
    else:
        return "That's not a suit symbol."


def new_enemy(enemy_list):
    current_baddie = enemy_list.pop()
    if current_baddie[0] == "J":
        return {"Name": f"Jack of {suit_interpreter(current_baddie[1], "J")}", "Blocks": f"{current_baddie[1]}",
                "health": 20, "damage": 10, "this_attack": 10, "card": current_baddie}
    if current_baddie[0] == "Q":
        return {"Name": f"Queen of {suit_interpreter(current_baddie[1], "Q")}", "Blocks": f"{current_baddie[1]}",
                "health": 30, "damage": 15, "this_attack": 15, "card": current_baddie}
    if current_baddie[0] == "K":
        return {"Name": f"King of {suit_interpreter(current_baddie[1], "K")}", "Blocks": f"{current_baddie[1]}",
                "health": 40, "damage": 20, "this_attack": 20, "card": current_baddie}


def draw_cards(draw_pile, hand, number_of_cards=1, max_hand_size=8, hands=None):
    if hands:
        current_player = 0
        for player in hands:
            if hand == player:
                break
            else:
                current_player += 1
        for number in range(number_of_cards):
            if len(draw_pile) > 0:
                for _ in hands:
                    if not len(hands[current_player]) < max_hand_size:
                        if current_player == len(hands) - 1:
                            current_player = 0
                        else:
                            current_player += 1
                if not len(hands[current_player]) < max_hand_size:
                    break
                drawn_card = draw_pile.pop()
                placed = False
                counter = 0
                while not placed:
                    if counter >= len(hands[current_player]):
                        hands[current_player].append(drawn_card)
                        placed = True
                    elif drawn_card[0] == "A" or drawn_card[0] == "Jes":
                        hands[current_player].insert(0, drawn_card)
                        placed = True
                    elif drawn_card[0] in ["J", "Q", "K"]:
                        hands[current_player].append(drawn_card)
                        placed = True
                    elif (hands[current_player][counter][0] != "A" and (
                            hands[current_player][counter][0] in ["J", "Q", "K"] or
                            hands[current_player][counter][0] >= drawn_card[0])):
                        hands[current_player].insert(counter, drawn_card)
                        placed = True
                    counter += 1
                if current_player == len(hands) - 1:
                    current_player = 0
                else:
                    current_player += 1
    else:
        for number in range(number_of_cards):
            if len(hand) < max_hand_size and len(draw_pile) > 0:
                drawn_card = draw_pile.pop()
                placed = False
                counter = 0
                while not placed:
                    if counter >= len(hand):
                        hand.append(drawn_card)
                        placed = True
                    elif drawn_card[0] == "A" or drawn_card[0] == "Jes":
                        hand.insert(0, drawn_card)
                        placed = True
                    elif drawn_card[0] in ["J", "Q", "K"]:
                        hand.append(drawn_card)
                        placed = True
                    elif (hand[counter][0] != "A" and hand[counter][0] != "Jes" and (hand[counter][0] in ["J", "Q", "K"] or
                            hand[counter][0] >= drawn_card[0])):
                        hand.insert(counter, drawn_card)
                        placed = True
                    counter += 1
    return hand


def input_parser(jester_uses, draw_pile, current_baddie, hand, discard_pile, user_input, hands=None):
    user_input = "".join(set(list(user_input)))
    number_of_cards = len(user_input)
    if "9" in user_input:
        if jester_uses > 0:
            jester(draw_pile, hand, discard_pile)
            jester_uses -= 1
            return jester_uses
        else:
            return f"{input_color("Out of Jester uses", "RED")}"
    elif "8" in user_input:
        return attack(draw_pile, current_baddie, hand, hands, discard_pile)
    elif number_of_cards == 1:
        try:
            return attack(draw_pile, current_baddie, hand, hands, discard_pile,
                          hand[int(user_input)])
        except IndexError:
            return input_color("You don't have that card", "RED")
    elif number_of_cards == 2:
        try:
            return attack(draw_pile, current_baddie, hand, hands, discard_pile,
                          hand[int(user_input[0])], hand[int(user_input[1])])
        except IndexError:
            return input_color("You don't have that card", "RED")
    elif number_of_cards == 3:
        try:
            return attack(draw_pile, current_baddie, hand, hands, discard_pile,
                          hand[int(user_input[0])], hand[int(user_input[1])],
                          hand[int(user_input[2])])
        except IndexError:
            return input_color("You don't have that card", "RED")
    elif number_of_cards == 4:
        try:
            return attack(draw_pile, current_baddie, hand, hands, discard_pile,
                          hand[int(user_input[0])], hand[int(user_input[1])],
                          hand[int(user_input[2])], hand[int(user_input[3])])
        except IndexError:
            return input_color("You don't have that card", "RED")
    else:
        return input_color("Wrong amount of choices", "RED")


def jester(draw_pile, hand, discard_pile):
    while len(hand) > 0:
        discarded_card = hand.pop(0)
        discard_pile.append(discarded_card)
    draw_cards(draw_pile, hand, 8)


def add_card(card, large_royal_played):
    current_value = card[0]
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


def attack(draw_pile, current_baddie, hand, hands, discard_pile, *user_input):
    attack_value = 0
    previous_value = 0
    multiplier = 1
    heals = False
    draws = False
    shield = False
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
        if card[1] == input_color("♠", "BLACK", "WHITE") and current_baddie["Blocks"] != input_color("♠", "BLACK",
                                                                                                     "WHITE"):
            shield = True
        elif card[1] == input_color("♥", "RED", "WHITE") and current_baddie["Blocks"] != input_color("♥", "BLACK",
                                                                                                     "WHITE"):
            heals = True
        elif card[1] == input_color("♣", "BLACK", "WHITE") and current_baddie["Blocks"] != input_color("♣", "BLACK",
                                                                                                       "WHITE"):
            multiplier = 2
        elif card[1] == input_color("♦", "RED", "WHITE") and current_baddie["Blocks"] != input_color("♦", "RED",
                                                                                                     "WHITE"):
            draws = True
        previous_value = int(current_value)
    for card in user_input:
        hand.remove(card)
    if draws:
        if not hands:
            draw_cards(draw_pile, hand, attack_value)
        else:
            draw_cards(draw_pile, hand, attack_value, 9 - len(hands), hands)
    if heals:
        for number in range(attack_value):
            if len(discard_pile) > 0:
                drawn_card = random.choice(discard_pile)
                discard_pile.remove(drawn_card)
                draw_pile.insert(0, drawn_card)
    if shield:
        current_baddie["this_attack"] -= attack_value
    for card in user_input:
        discard_pile.append(card)
    current_baddie["health"] -= (attack_value * multiplier)
    return current_baddie


def block_attack(current_baddie, hand, card, discard_pile):
    if len(hand) > 0:
        block, _ = add_card(card, False)
        current_baddie["this_attack"] -= block
        discard_pile.append(card)
        hand.remove(card)
        return current_baddie
    else:
        return "Game Over"


def ui_display(current_baddie, draw_pile, discard_pile, jester_uses, hand):
    print(f"See the rules at any time by pressing enter."
          f"\n\n{current_baddie["Name"]}")
    print(
        f"Health: {input_color(current_baddie["health"], "WHITE", "RED")}\tDamage: {input_color(current_baddie["damage"], "WHITE", "RED")}\t")
    print(f"\nJesters:\t{jester_uses} Jesters left")
    print(f"Draw pile:\t{len(draw_pile)} cards left")
    print("Discard pile:", end="\t")
    if len(discard_pile) != 0:
        print(f"{len(discard_pile)} cards in total with "
              f"{input_color([discard_pile[-1] if len(discard_pile) > 0 else "nothing"][0][0], "BLACK", "WHITE")}"
              f"{[discard_pile[-1] if len(discard_pile) > 0 else ""][0][1]} as the top card")
    else:
        print("Empty")
    print("\nYour hand:")
    for number in range(len(hand)):
        print(f"{number}: {input_color(hand[number][0], "BLACK", "WHITE")}{hand[number][1]}",
              end="\t")
    print("8: Yield  9: Jester")


def game():
    draw_pile = new_deck()
    random.shuffle(draw_pile)
    baddies = enemies()
    current_baddie = new_enemy(baddies)
    hand = []
    discard_pile = []
    draw_cards(draw_pile, hand, 8)
    jester_uses = 2
    game_end = False
    exception = False
    while not game_end:
        os.system('cls||clear')
        if exception:
            print(exception)
        else:
            print("")
        exception = False
        if len(hand) == 0 and jester_uses == 0:
            print("Game Over")
            break
        user_input = False
        ui_display(current_baddie, draw_pile, discard_pile, jester_uses, hand)
        while not user_input:
            user_input = input(f"{input_color("You are attacking!", "YELLOW")}\n").strip()
            action = ""
            try:
                int(user_input)
            except ValueError:
                os.system('cls||clear')
                print(HELPTEXT)
                input("Press enter to go back to the game:")
                break
            if user_input:
                action = input_parser(jester_uses, draw_pile, current_baddie, hand, discard_pile, user_input)
            if type(action) == str:
                exception = action
            elif type(action) == int:
                jester_uses = action
            elif type(action) == dict:
                current_baddie = dict(action)
                if int(current_baddie["health"]) <= 0:
                    discard_pile.append(current_baddie["card"])
                    if len(baddies) > 0:
                        current_baddie = new_enemy(baddies)
                    else:
                        if jester_uses == 2:
                            print(f"{input_color(" Gold Victory! ", "YELLOW", "BLACK")}")
                        elif jester_uses == 1:
                            print(f"{input_color(" Silver Victory! ", "DARK_GRAY", "WHITE")}")
                        else:
                            print(f"{input_color(" Bronze Victory! ", "WHITE", "BLACK")}")
                        game_end = True
                        break
                else:
                    exception = False
                    while current_baddie["this_attack"] > 0:
                        os.system('cls||clear')
                        if exception:
                            print(exception)
                        else:
                            print("")
                        if len(hand) == 0 and jester_uses == 0:
                            print("Game Over")
                            game_end = True
                            break
                        ui_display(current_baddie, draw_pile, discard_pile, jester_uses, hand)
                        card = str(input(f"{input_color("You are defending!", "BRIGHT_BLUE")}\tBlock {current_baddie["this_attack"]} damage\n")).strip()
                        if card == "9" and jester_uses != 0:
                            jester(draw_pile, hand, discard_pile)
                            jester_uses -= 1
                        else:
                            try:
                                current_baddie = block_attack(current_baddie, hand, hand[int(card[0])], discard_pile)
                                exception = False
                            except IndexError:
                                exception = input_color("You don't have that card", "RED")
                            except ValueError:
                                exception = input_color("Wrong input", "RED")
                        if type(current_baddie) == str:
                            print(current_baddie)
                            break
                    current_baddie["this_attack"] = current_baddie["damage"]


def multiplayer_jester(players, current_player, current_baddie, undecided=True):
    current_baddie["Blocks"] = False
    choice = 0
    if current_baddie["Name"][0] == "J":
        current_baddie["Name"] = "Jack of Sadness :("
    if current_baddie["Name"][0] == "Q":
        current_baddie["Name"] = "Queen of Sorrow :("
    if current_baddie["Name"][0] == "K":
        current_baddie["Name"] = "King of Pity :("
    print("\nYou disabled the Royal's suit!")
    while undecided:
        try:
            choice = int(input(f"you are player {current_player} which player 0-{players - 1} should go next?"))
        except ValueError:
            print("please type an integer.")
        if choice != current_player and players > choice > 0:
            undecided = False
        else:
            print("invalid choice")
    return choice, current_baddie

def multiplayer(players):
    jester_uses = 0
    draw_pile = new_deck()
    if players > 2:
        draw_pile.append(("Jes", input_color("ter", "RED", "WHITE")))
    if players > 3:
        draw_pile.append(("Jes", input_color("ter", "BLACK", "WHITE")))
    random.shuffle(draw_pile)
    baddies = enemies()
    current_baddie = new_enemy(baddies)
    discard_pile = []
    each_player_hand = []
    for player_number in range(players):
        each_player_hand.append(draw_cards(draw_pile, [], 8, 9 - players))
    game_end = False
    exception = False
    current_player = 0
    while not game_end:
        hand = each_player_hand[current_player]
        os.system('cls||clear')
        if exception:
            print(exception)
        else:
            print("")
        exception = False
        if len(hand) == 0:
            print("Game Over")
            break
        user_input = False
        ui_display(current_baddie, draw_pile, discard_pile, 0, hand)
        while not user_input:
            user_input = input(f"{input_color("You are attacking!", "YELLOW")}\n").strip()
            action = "Jester played"
            try:
                int(user_input)
            except ValueError:
                os.system('cls||clear')
                print(HELPTEXT)
                input("Press enter to go back to the game:")
                break
            if user_input:
                if hand[int(user_input[0])][0] == "Jes":
                    current_player, current_baddie = multiplayer_jester(players, current_player, current_baddie)
                    hand.remove(hand[int(user_input[0])])
                    break
                else:
                    action = input_parser(0, draw_pile, current_baddie, hand, discard_pile, user_input, each_player_hand)
            if type(action) == str:
                exception = action
            elif type(action) == int:
                jester_uses = action
            elif type(action) == dict:
                current_baddie = dict(action)
                if int(current_baddie["health"]) <= 0:
                    discard_pile.append(current_baddie["card"])
                    if len(baddies) > 0:
                        current_baddie = new_enemy(baddies)
                    else:
                        print(f"{input_color(" Victory! ", "WHITE", "BLACK")}")
                        game_end = True
                        break
                else:
                    exception = False
                    while current_baddie["this_attack"] > 0:
                        os.system('cls||clear')
                        if exception:
                            print(exception)
                        else:
                            print("")
                        if len(hand) == 0 and jester_uses == 0:
                            print("Game Over")
                            game_end = True
                            break
                        ui_display(current_baddie, draw_pile, discard_pile, jester_uses, hand)
                        card = str(input(
                            f"{input_color("You are defending!", "BRIGHT_BLUE")}\tBlock {current_baddie["this_attack"]} damage\n")).strip()
                        if card == "9" and jester_uses != 0:
                            jester(draw_pile, hand, discard_pile)
                            jester_uses -= 1
                        else:
                            try:
                                current_baddie = block_attack(current_baddie, hand, hand[int(card[0])], discard_pile)
                                exception = False
                            except IndexError:
                                exception = input_color("You don't have that card", "RED")
                            except ValueError:
                                exception = input_color("Wrong input", "RED")
                        if type(current_baddie) == str:
                            print(current_baddie)
                            break
                    current_baddie["this_attack"] = current_baddie["damage"]
            if current_player == players - 1:
                current_player = 0
            else:
                current_player += 1


def main():
    print(HELPTEXT)
    players = False
    while not players:
        try:
            players = int(input("How many players are playing"))
        except ValueError:
            print("please type an integer from 1-4:")
        if 1 > players or players > 4:
            players = False
            print("please type an integer from 1-4:")
    if players == 1:
        game()
    else:
        multiplayer(players)


if __name__ == "__main__":
    main()