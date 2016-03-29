'''input is used to get the input for the transportation problem.
It has four methods: getInput(), getCost(), getDemand(), getSupply().
'''
import numpy as np
supply =list()
demand = list()
cost =0
def getInput():
    '''getInput takes no argument.
    It is used to get the input from the standard input.'''
    row =int(raw_input("Enter the number of rows: "))
    column =int(raw_input("Enter the number of columns: "))
    global cost
    cost = np.zeros(shape=(row,column),dtype=np.int)
    global supply
    global demand
    print "Enter the supply"
    for i in range(row):
	stm = "Enter the supply at %d  position "%(i)
	s = int(raw_input(stm))
	supply.append(s);

    print "Enter the demand"
    for i in range(column):
	stm = "Enter the demand at %d position"%(i)
	s = int(raw_input(stm))
	demand.append(s);
    def balance():
	diff = abs(sum(supply) -sum( demand))
	global cost
	if supply>demand:
		padding = np.zeros(shape=(row,1),dtype=np.int)
		cost =np.concatenate((cost, padding), axis=1)
		demand.append(diff)
	else:
		padding = np.zeros(shape=(1,column),dtype=np.int)
		cost =np.concatenate((cost, padding), axis=0)
		supply.append(diff)
		

    if sum(supply) == sum(demand):
	pass
    else:
	balance()

    for r in range(row):
	for c in range(column):
		stm = "Enter the cost fo transportation at [%d] : [%d] "%(r,c)
		cos = int(raw_input(stm))
		cost[r][c] = cos

def getSupply():
    global supply
    return supply
def getCost():
    global cost
    return cost
def getDemand():
    global demand
    return demand


