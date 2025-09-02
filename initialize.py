from art import input_color


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