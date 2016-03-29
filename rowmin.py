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
    print"Inside init"
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
    print"Inside allocate"
    rowmin = cost.min(1)
    temp = deepcopy(cost)
    row = 0
    s = copy(supply)
    d= copy(demand)
    while sum(s) != 0 and sum(d) != 0:
        c=0
        temp = np.matrix(temp)
        r,c = np.where(temp[row] == rowmin[row])
        temp = np.array(temp)
        r = np.array(r)
        c= np.array(c)
        r = int(r[0][0])
        c = int(c[0][0])
        temp [row] [c] = 5 ** 12
        rowmin = temp.min(1)
        if s[row] == 0:
            row += 1
        elif d[c] == 0:
            continue
        elif s[row] > 0 and d[c] > 0:
            price = min(s[row], d[c])
            global allocation
            allocation[row][c] = price
            s[row] -= price
            d[c] -= price
            if s[row] == 0:
                row+=1
    print "Allocation:\n",allocation

def transcost():
    global allocation
    global cost
    tcost = np.multiply(cost,allocation)
    tcost = tcost.sum()
    print "Transport cost: ", tcost