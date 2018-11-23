file = open('geneticConfig.txt','r')
config = file.readlines()

columns = config[1]
rows = config[3]
transportCostMatrix = config[7]
neighbourPunishmentMatrix = config[9]
startingPopulation = config[15]
parentSelectionMode = [18]
crossoverOperator = config[21]
mutationProbability = config[24]
mutationOperator = config[27]
successionMode = [30]

print(neighbourPunishmentMatrix)
file.close()

