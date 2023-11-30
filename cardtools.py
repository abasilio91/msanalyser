import pandas as pd
import random

def get_past_games():
    df = pd.read_csv('raw_resultados.csv')
    df['past_games'] = df.apply(lambda x: list([x['num1'],
                                                x['num2'],
                                                x['num3'],
                                                x['num4'],
                                                x['num5'],
                                                x['num6']]), axis=1)
    return df.past_games.to_list()

def create_naive_cards(num_per_card: int=6, num_cards: int=1) -> list:
    games = []
    while len(games) < num_cards:
        card = random.sample(range(1,61), num_per_card)
        card.sort()
        if not card_exists(card):
            games.append(card)
    return games

def card_exists(card):
    past_games = get_past_games()
    if card in past_games:
        return True
    return False    

def create_cards_in_range(num_range: dict=None, num_cards: int=1, num_per_card: int=6):
    if not num_range:
        return create_naive_cards(num_per_card, num_cards)
    
    games = []
    while len(games) < num_cards:
        card = []    
        for _, value in num_range.items():
            card.append(random.choice(value))
        
        if not card_exists(card):
            games.append(card)
    return games