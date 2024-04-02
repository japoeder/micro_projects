Name: Jonathan Poeder, JHEDID jpoeder1
Module Info: 
	-Module 14 Assignment: Quantum Computing
	-Due: 12/14/2021 at 11:59 EST
Approach:

While skeleton code wasn't provided for the final exam, a
general outline was provided in the assignment pdf.  My
approach was simply to follow that guide and fill in the
gaps where necessary.

General Steps:
***main.py***
1) Import modules
2) Import & pre-process qubits
3) Instantiate some items
4) Split the record from the data
5) Append ket elements to corresponding list
6) Append gate elements to corresponding list
7) Pars dictionary for data of interest
8) Test amplitudes
9) Next lets check the gates (can call paulix or hadamard)
10) If both tests pass, run gate operations
11) Print the final state information
12) Run the binomial experiment method

***qubit.py***
1) Import modules
2) Create the exception class for invalid prob amps
3) Define qubit constructor
4) Only run the amplitude validation when flagged
5) Method to calculate the probability amplitudes
6) This is the square of alpha and the square of beta
7) Return tuple with the probability of 0 or 1 qubit from a measurement
8) Method to validate the amplitudes
9) Run prob amp calculation
10) Need to ensure alpha and beta sum of squares equals 1
11) Raise error when the sum of squares doesn't equal one, but include some tolerance
12) Run binomial dist experiment
13) Only need to choose one of the states' prob amps, choosing second
14) Sample the binomial distribution n=1 times in 1000 experiments
15) Calculate the ratio to get % of 1s
16) 1 minus one_p to get % of 0s
17) Stick in a dictionary and return
18) If no processed states, grab from original list to print
19) If processed states, grab from numpy array
20) Deal with small amplitude numbers

***operators.py***
1) Create exception class for invalid operators
2) Class for testing qubit operator
3) Loop through provided matrix and if operation isn't X or H, raise exception

***paulix.py & hadamard.py***
1) Run imports
2) Create class for paulix operator, inherit from SingleQubitOperator
3) If a list of operators is provided, validate with SingleQubitOperator
4) Define method for operator calculation

Known Bugs:
N/A - the code produces the desired results.