from load import *
import pandas as pd

def mon_id_to_mon_name(mon_id: int) -> str:
    MONS[(MONS['id']==mon_id) & (MONS['is_default'] == 1)]

def mon_id_series_to_mon_name_series(mon_id_series: pd.Series) -> pd.Series:
    return MONS[(MONS['id'].isin(mon_id_series)) & (MONS['is_default'] == 1)]['identifier']

