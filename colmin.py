import input
from copy import deepcopy,copy
import numpy as np
cost = 0
supply = []
demand = []
row = 0
column = 0
allocation = 0
def init():
    '''This method is used to initialize all the global variables.
    All the variables are obtained from the input module'''
    #input.getInput()
    global cost
    cost = input.getCost()
    global supply
    supply = input.getSupply()
    global demand
    demand = input.getDemand()
    global row
    row = len(supply)
    global column
    column = len(demand)
    global allocation
    allocation = np.zeros(shape=(row, column))


def allocate():
    colmin = cost.min(0)
    temp = deepcopy(cost)
    col = 0
    s = copy(supply)
    d= copy(demand)
    while sum(s) != 0 and sum(d) != 0:
        r=0
        temp = np.matrix(temp)
        r,c = np.where(temp[:,col] == colmin[col])
        temp = np.array(temp)
        r = np.array(r)
        c= np.array(c)
        r = int(r[0][0])
        c = int(c[0][0])
        temp [r] [col] = 5 ** 12
        colmin = temp.min(0)
        if s[r] == 0:
            continue
        elif d[col] == 0:
            col+=1
        elif s[r] > 0 and d[col] > 0:
            price = min(s[r], d[col])
            global allocation
            allocation[r][col] = price
            s[r] -= price
            d[col] -= price
            if d[col] == 0:
                col+=1
    print "Allocation:\n",allocation


def transcost():
    global cost, allocation
    tcost = np.multiply(cost,allocation)
    tcost = tcost.sum()
    print "Transport cost: ", tcost