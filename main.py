from datamacro import recuperation_df
from estimation import estimate_parameters
from sympy import symbols, Eq, solve
import numpy as np
import matplotlib.pyplot as plt


# Définir les variables
Y, C, I, G, T, M, P, r, L, Y_L, i, LM, IS = symbols('Y C I G T M P r L Y_L i LM IS')

# Définir les paramètres
c0, c1, b, h, k, m1, m2 = symbols('c0 c1 b h k m1 m2')

#Définir les équations comportementales
# Equation de consommation (C)
C_eq = Eq(C, c0 + c1*(Y-T))

# Equation d'investissement (I)
I_eq = Eq(I, b - h*r)

# Equation de la demande de monnaie (L)
L_eq = Eq(L, k*Y - m1*i)

# Equation de l'offre de monnaie (M/P)
M_eq = Eq(M/P, L)

# Equation IS (Y = C + I + G)
IS_eq = Eq(Y, C + I + G)

# Equation LM (M/P = L)
LM_eq = Eq(M/P, L)


pibn=recuperation_df("pibn")
pibr=recuperation_df("pibr")
ogt=recuperation_df("ogt")
bop=recuperation_df("bop")
mon=recuperation_df("mon")
taux=recuperation_df("interet")
#print(type(ogt))
#print(ogt.dtypes)
#print(pibn.columns)

# Transformer les données en utilisant le logarithme népérien
ogt['T'] = np.log(ogt['OGT_Impots '])
pibr['Y'] = np.log(pibr["CNR_PIB aux prix d'acquisition"])
pibn['Yn'] = np.log(pibn["CNN_PIB aux prix d'acquisition"])

#Crrer le dataframe df pour l'analyse
    #Ajout de PIB reel Y
df = pibr['Y'].copy()
df = df.to_frame()

    #Ajout deflateur P 
deflateur = pibn['Yn']/pibr['Y']
log_deflateur = np.log(deflateur)
df['P'] = log_deflateur

    #Ajout consommation C
consommation=pibr['CNR_Dépenses de consommation finale des Ménages ']
df['C']=np.log(consommation)

    #Ajout de l'Investissement I
invessisement=pibr["CNR_Formation brute de capital"]
df['I']=np.log(invessisement)

    #Ajout de Gouvernement G
gouvernement=pibr["CNR_Dépenses_consommation_finale_Administrations"] 
df['G']=np.log(gouvernement)

recettes=ogt["OGT_Recettes fiscales brutes"]/deflateur
df['T']=np.log(recettes)

    #Ajout masse monetaire M
monnaie=mon["SM_AgrégatM3"]
df['M']=np.log(monnaie)

    #Ajout interet r et i
df["r"]=taux["interetr"]
df["i"]=taux["interetn"]

# Créer une nouvelle colonne pour Y - T
df['Y_minus_T'] = df['Y'] - df['T']


#Estimation equations de comportement

# Estimation de l'équation de consommation
consumption_params = estimate_parameters(df['C'], df[['Y_minus_T']])
c0_estimated = consumption_params[0]  # intercept
c1_estimated = consumption_params[1]  # coefficient de Y-T

# Estimation de l'équation d'investissement
investment_params = estimate_parameters(df['I'], df[['r']])
b_estimated = investment_params[0]  # intercept
h_estimated = -investment_params[1]  # coefficient de r

# Estimation de l'équation de demande de monnaie
money_demand_params = estimate_parameters(df['M'] - df['P'], df[['Y', 'i']])
k_estimated = money_demand_params[1]  # coefficient de Y
m1_estimated = -money_demand_params[2]  # coefficient de i 


# Définir les équations IS et LM estimées
IS_eq_estimated = Eq(Y, c0_estimated + c1_estimated*(Y-T) + b_estimated - h_estimated*r + G)
LM_eq_estimated = Eq(M/P, k_estimated*Y - m1_estimated*i)

# Résoudre le système d'équations
equilibrium_values = solve((IS_eq_estimated, LM_eq_estimated), (Y, r))

# Afficher les valeurs d'équilibre pour Y et r
print(f"Equilibrium Y: {equilibrium_values[Y]}")
print(f"Equilibrium r: {equilibrium_values[r]}")


# Les valeurs prévues pour G, T, M, P et i pour 2022, 2023 et 2024.
# Vous devrez les remplacer par vos propres prévisions.
future_values = {
    2022: {"G": 8, "T": 7, "M": 9, "P": 0.01, "i": 0.4},
    2023: {"G": 8, "T": 7, "M": 9, "P": 0.01, "i": 0.4},
    2024: {"G": 8, "T": 7, "M": 9, "P": 0.01, "i": 0.4},
}

# Créez des listes vides pour stocker les valeurs simulées de Y et r
simulated_Y = []
simulated_r = []

# Bouclez sur les années futures et simulez les valeurs de Y et r
for year, values in future_values.items():
    simulated_Y.append(equilibrium_values[Y].subs(values).evalf())
    simulated_r.append(equilibrium_values[r].subs(values).evalf())

# Affichez les valeurs simulées
print("Simulated Y:", simulated_Y)
print("Simulated r:", simulated_r)

# Créez une figure et un axe
fig, ax = plt.subplots()

# Tracez les valeurs simulées de Y
ax.plot(list(future_values.keys()), simulated_Y, label='Y')

# Tracez les valeurs simulées de r
ax.plot(list(future_values.keys()), simulated_r, label='r')

# Ajoutez une légende
ax.legend()

# Affichez le graphique
plt.show()