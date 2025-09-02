from art import suit_interpreter


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
    return None


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
                    elif (hands[current_player][counter][0] != "A" and hand[counter][0] != "Jes"
                          and (hands[current_player][counter][0] in ["J", "Q", "K"] or
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
                    elif (hand[counter][0] != "A" and hand[counter][0] != "Jes" and (
                            hand[counter][0] in ["J", "Q", "K"] or
                            hand[counter][0] >= drawn_card[0])):
                        hand.insert(counter, drawn_card)
                        placed = True
                    counter += 1
    return hand


def jester(draw_pile, hand, discard_pile):
    while len(hand) > 0:
        discarded_card = hand.pop(0)
        discard_pile.append(discarded_card)
    draw_cards(draw_pile, hand, 8)



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
        if choice != current_player and players > choice >= 0:
            undecided = False
        else:
            print("invalid choice")
    return choice, current_baddie