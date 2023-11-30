import pandas as pd
import random

def create_naive_cards(num_per_card: int=6, num_cards: int=1) -> list:
    games = []
    past_games = get_past_games()
    while len(games) < num_cards:
        card = random.sample(range(1,61), num_per_card)
        card.sort()
        if not card_exists(card, past_games):
            games.append(card)
    return games

def card_exists(card, past_games):
    if card in past_games:
        return True
    return False    

print(create_naive_cards(6, 7))