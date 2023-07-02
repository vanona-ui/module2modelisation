from datamacro import recuperation_df
from estimation import estimate_parameters

pibn=recuperation_df("pibn")
ogt=recuperation_df("ogt")

#print(type(ogt))
#print(ogt.dtypes)
#print(pibn.columns)

params = estimate_parameters(ogt["OGT_Impots "], pibn["CNN_PIB aux prix d'acquisition"])

print(params)


