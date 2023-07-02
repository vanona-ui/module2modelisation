import pandas as pd
import numpy as np

def recuperation_df(sheet):
    # Lire les données Excel
    df = pd.read_excel('F:\module2modelisation\datamacro\data.xlsx', sheet_name=sheet)

    # Définir la première colonne (0) comme index du DataFrame
    df.set_index(df.columns[0], inplace=True)

    # Transposer le DataFrame pour avoir les années comme index
    df = df.transpose()

    # Remplacez '…' par NaN avant de convertir en float
    df = df.replace('…', np.nan)

    # Remplacer les virgules par des points et convertir en float
    df = df.replace(',', '.', regex=True).astype(float)

    #Cela transformera vos années en dates datetime
    df.index = pd.to_datetime(df.index, format='%Y')

    return df

""" dg=recuperation_df()
print(dg['OGT_Dépenses en capital'])
print(dg.columns) """
