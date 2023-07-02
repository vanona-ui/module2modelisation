from datamacro import recuperation_df
from estimation import estimate_parameters

pibn=recuperation_df("pib_nominal")
ogt=recuperation_df("OGT")

params = estimate_parameters(ogt[''], ['X1', 'X2'])
print(params)


