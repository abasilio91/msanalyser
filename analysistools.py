#%%
import pandas as pd
from cardtools import *

#%%
def create_percentage_df(df):
    percentage = pd.DataFrame(range(1,61), columns=['numero'])
    for i in range(6):
        aux = df[f'num{i+1}'].value_counts(normalize=True)*100
        aux = pd.DataFrame({f'num{i+1}':aux})
        aux['numero'] = aux.index
        percentage = percentage.merge(aux, on='numero', how='left')
        percentage = percentage.fillna(0)

    return percentage

def most_common_range(df, ball):
    return df[['numero', ball]].sort_values(by=ball,ascending=False)[:10]

# %%
