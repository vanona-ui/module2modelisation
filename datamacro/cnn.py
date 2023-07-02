import pandas as pd

# Lisez les données à partir du fichier Excel
df = pd.read_excel("data.xlsx", index_col=0)

# Transformez les données de format large à format long
df = df.melt(var_name="Annee", value_name="Valeur")

# Convertissez la colonne "Annee" en type datetime
df["Annee"] = pd.to_datetime(df["Annee"], format="%Y")

# Réindexez le DataFrame avec la colonne "Annee"
df.set_index("Annee", inplace=True)

# Maintenant, 'df' est une série temporelle annuelle.

print(df)
