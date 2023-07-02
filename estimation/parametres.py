

import statsmodels.api as sm
import pandas as pd

def estimate_parameters(dependent_var, *independent_vars):
    # Ajouter une constante à notre ensemble de variables indépendantes
    X = sm.add_constant(pd.concat(independent_vars, axis=1))
    
    # Créer le modèle MCO
    model = sm.OLS(dependent_var, X)
    
    # Estimer les paramètres
    results = model.fit()
    
    # Renvoyer les paramètres estimés
    return results.params
