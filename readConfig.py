file = open('geneticConfig.txt','r')
config = file.readlines()

columns = config[1]
rows = config[3]
transportCostMatrix = config[6]
neighbourPunishmentMatrix = config[9]
startingPopulation = config[14]
parentSelectionMode = config[17]
crossoverOperator = config[20]
mutationProbability = config[23]
mutationOperator = config[26]
successionMode = config[29]

file.close()

