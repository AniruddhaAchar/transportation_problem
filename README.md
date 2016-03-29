# transportation problem
Implementation of 3 basic transportation algorithm in python using numpy

The repository contains 5 modules.
  1. input.py: This module takes the input i.e. the cost, supply and demand. In this module, there is a method to balance unbalanced transportation problem.
  2. northwest.py: This module has 3 importation
    1. init(): this will initialize all cost, supply, demand and allocation matrix.
    2. allocate(): This will allocate the from which factory to which warehouse the comodity needs to be moves so as to incur minimum cost. This is done using the north west corner rule for allocation.
    3.transcost(): This method calculates the transportation cost for the allocation.
  3. rowmin.py: This is used to calculate the transportation based on row minimum method. The functions are similar to northwest.py
  4. colmin.py: This is used to calculate the transportation based on colum minimum method. The functions are similar to northwest.py
  5. main.py: Ths module is used to call and test all the modules.
