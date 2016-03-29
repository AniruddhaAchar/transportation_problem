import input
import numpy as np
cost = 0
supply = []
demand = []
row = 0
column = 0
allocation = 0


def getAllocation():
    global allocation
    return allocation


def allocate():
    '''This method allocateds which routs needs to be taken based on the NWCR'''
    trow = 0
    tcol = 0
    while trow != row and tcol != column:
        global allocation
        alloc = min(supply[trow], demand[tcol])
        supply[trow] -= alloc
        demand[tcol] -= alloc
        allocation[trow][tcol] = alloc
        if (supply[trow] == 0):
            trow += 1
        else:
            tcol += 1
    print "Allocation: ",allocation


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
    #print "Allocation:\n",allocation
def transcost():
     tcost = np.multiply(cost,allocation)
     tcost = tcost.sum()
     print "Transport cost: ", tcost