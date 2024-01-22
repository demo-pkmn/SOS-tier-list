from load import ABILITIES, MON_ABILITIES
from mon_funcs import mon_id_series_to_mon_name_series
import pandas as pd
from typing import List
from functools import reduce

def ability_name_to_id(ability_name: str) -> int:
    return ABILITIES[ABILITIES['name']==ability_name]['ability_id'].iloc[0]

def ability_id_to_mon_id_series(ability_id: int) -> pd.Series:
    return MON_ABILITIES[MON_ABILITIES['ability_id']==ability_id]['pokemon_id']

def ability_list():
    return ABILITIES[(ABILITIES['local_language_id']==9) & (ABILITIES['ability_id']<10000)]['name'].tolist()

def ability_list_to_mon_name_series(ability_list: List[str]) -> pd.Series:
    if not ability_list: return None
    mon_id_series_list = [ability_id_to_mon_id_series(
            ability_name_to_id(ability_name)
        ) for ability_name in ability_list
    ]
    mon_id_series = reduce(lambda x, y: pd.Series(list(set(x) & set(y))), mon_id_series_list)
    return mon_id_series_to_mon_name_series(mon_id_series).values