import pandas as pd

MONS = pd.read_csv('pokemon.csv')
MOVES = pd.read_csv('move_names.csv')
ABILITIES = pd.read_csv('ability_names.csv')
TYPES = pd.read_csv('types.csv')

MON_ABILITIES = pd.read_csv('pokemon_abilities.csv')
MON_MOVES = pd.read_csv('pokemon_moves.csv')
MON_TYPES = pd.read_csv('pokemon_types.csv')

TIERLIST = pd.read_csv('tierlist.csv')
PICKED = pd.read_csv('picked.csv', header=None)