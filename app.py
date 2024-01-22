import pandas as pd
import streamlit as st
from load import *

from ability_funcs import ability_list, ability_list_to_mon_name_series
from type_funcs import type_list, type_list_to_mon_name_series
from move_funcs import move_list, move_list_to_mon_name_series

def highlight(mon: str):
    if mon is None:
        return
    for filter in ['move', 'type', 'ability']:
        if mon.lower() not in ss.results.get(filter, []) and ss.filter.get(filter, False) and ss.results.get(filter, []):
            return 'background-color: #593c36'
        if mon in PICKED.values and ss.filter['picked']:
            return 'background-color: #593c36'
    return 'background-color: #365953'

def load_df():
    pivot_df = TIERLIST.groupby('points')['name'].agg(list).reset_index()
    d={}
    for _, (points,name) in pivot_df.iterrows():
        d[points]=name
    df = pd.DataFrame.from_dict(d, orient='index').T

    return df[sorted(df.columns, key=int, reverse=True)]

st.set_page_config(layout="wide")
ss=st.session_state
if "filter" not in ss:
    ss.filter = {}
if "results" not in ss:
    ss.results = {}


# with st.expander("DataFrames"):
#     MON_MOVES
#     MON_TYPES
#     MON_ABILITIES
#     MOVES
#     MONS
#     ABILITIES
#     TYPES
#     TIERLIST
#     PICKED

df=load_df()

selected_moves = st.multiselect('Select moves', move_list())
selected_types = st.multiselect('Select types', type_list(), max_selections=2)
selected_abilities = st.multiselect('Select abilities', ability_list())

# st.write(selected_abilities, selected_moves, selected_types)
if selected_moves:
    ss.results['move']=move_list_to_mon_name_series(selected_moves)
if selected_types:
    ss.results['type']=type_list_to_mon_name_series(selected_types)
if selected_abilities:
    ss.results['ability']=ability_list_to_mon_name_series(selected_abilities)
# st.write(ss.results['move'], ss.results['type'], ss.results['ability'])

ss.filter['move'] = st.checkbox("Filter by move?")
ss.filter['type'] = st.checkbox("Filter by type?")
ss.filter['ability'] = st.checkbox("Filter by ability?")
ss.filter['picked'] = st.checkbox("Filter picked Pokemons?", value=True)

st.dataframe(df.style.applymap(highlight), height=35*(len(df.index)+1))
