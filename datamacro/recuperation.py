import pandas as pd

def recuperation_df(sheet):
    # Lisez les données à partir du fichier Excel
    df = pd.read_excel("F:\module2modelisation\datamacro\data.xlsx", sheet_name=sheet, index_col=0)

    # Transposez le DataFrame pour que chaque ligne représente une année
    df = df.transpose()

# Convertissez l'index en type datetime
    df.index = pd.to_datetime(df.index, format="%Y")

    return df

