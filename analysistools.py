import pandas as pd

def str_to_list_of_int(str):
    return [int(x) for x in str.replace("[","").replace("]","").replace('\n',"").split(sep=",")]

def create_df(file):
    df = pd.read_csv(file)
    return df

df = create_df('raw_resultados.csv')
string_numbers = str_to_list_of_int(df.numeros)
print(string_numbers)