from datamacro import recuperation_df
from estimation import estimate_parameters

pibn=recuperation_df("pib_nominal")
ogt=recuperation_df("OGT")


print(ogt.columns)


#params = estimate_parameters(ogt["OGT_Impots"], pibn["CNN_PIB aux prix d'acquisition"])

#print(params)


