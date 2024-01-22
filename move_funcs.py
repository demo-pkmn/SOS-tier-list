from load import MOVES, MON_MOVES
from mon_funcs import mon_id_series_to_mon_name_series
import pandas as pd
from functools import reduce

def move_name_to_id(move_name: str) -> int:
    return MOVES[MOVES['name']==move_name]['move_id'].iloc[0]

def move_id_to_mon_id_series(move_id: int) -> pd.Series:
    return MON_MOVES[MON_MOVES['move_id']==move_id]['pokemon_id']

def move_list() -> list[str]:
    return MOVES[(MOVES['local_language_id']==9) & (MOVES['move_id']<10000)]['name'].tolist()

def move_list_to_mon_name_series(move_list: list[str]) -> pd.Series:
    if not move_list: return None
    mon_id_series_list = [move_id_to_mon_id_series(
            move_name_to_id(move_name)
        ) for move_name in move_list
    ]
    mon_id_series = reduce(lambda x, y: pd.Series(list(set(x) & set(y))), mon_id_series_list)
    return mon_id_series_to_mon_name_series(mon_id_series).values
