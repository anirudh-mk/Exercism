"""Black Jack"""

def value_of_card(card):
    
    if 'J' in card or 'K' in card or 'Q' in card:
        return 10
    if 'A' in card:
        return 1
    return int(card)
    
def higher_card(card_one, card_two):

    if value_of_card(card_one) == value_of_card(card_two):
        return card_one, card_two
    if value_of_card(card_one) > value_of_card(card_two):
        return card_one
    return card_two


def value_of_ace(card_one, card_two):
    
    ace = value_of_card(card_one) + value_of_card(card_two)
    
    if ace >= 11 or 'A' in card_one or 'A' in card_two:
        return 1
    return 11

def is_blackjack(card_one, card_two):
    
    if card_one == 'A' or card_two == 'A':
        if (value_of_card(card_one) == 10) or (value_of_card(card_two) == 10):
            return True
        return False
    return False
    
def can_split_pairs(card_one, card_two):
    
    if value_of_card(card_one) is value_of_card(card_two):
        return True
    return False
    


def can_double_down(card_one, card_two):
    
    points = [9, 10, 11]
    return (value_of_card(card_one) + value_of_card(card_two)) in points