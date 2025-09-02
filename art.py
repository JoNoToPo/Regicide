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