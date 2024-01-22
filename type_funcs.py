from load import TYPES, MON_TYPES
from mon_funcs import mon_id_series_to_mon_name_series
import pandas as pd
from functools import reduce

def type_name_to_id(type_name: str) -> int:
    return TYPES[TYPES['identifier']==type_name]['id'].iloc[0]

def type_id_to_mon_id_series(type_id: int) -> pd.Series:
    return MON_TYPES[MON_TYPES['type_id']==type_id]['pokemon_id']

def type_list() -> list[str]:
    return TYPES[TYPES['id']<10000]['identifier'].tolist()

def type_list_to_mon_name_series(type_list: list[str]) -> pd.Series:
    if not type_list: return None
    mon_id_series_list = [type_id_to_mon_id_series(
            type_name_to_id(type_name)
        ) for type_name in type_list
    ]
    mon_id_series = reduce(lambda x, y: pd.Series(list(set(x) & set(y))), mon_id_series_list)
    return mon_id_series_to_mon_name_series(mon_id_series).values
