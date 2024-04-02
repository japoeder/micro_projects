Name: Jonathan Poeder, JHEDID jpoeder1
Module Info: 
	-Module 4: Data Structures
	-Module 4 Assignment: N-body Simulation
	-Due: 09/26/2021 at 11:59 EST
Approach:

I chose to define a function so I'd be able to simply provide 
any new set of bodies, total time, and steps to the function 
and have it run initial as well as simulated calculations. 
The steps for the program are broken out below.  After 
defining the function it is called by a loop that prints
the desired position, velocity, and mass values in the output
window.  Note that this does not account for the force of the
planetary body on the sun as instructed in the assignment
document.

General Steps:
1) Set t, dt, and G parameters for simulation
2) Create lists for each planetary body
3) Create nested list for looping later
4) Build function to run calculations
5) Break out coordinates for initial r calculation
6) Do the same for initial velocities and mass
7) Set counter for while loop
8) Begin while loop simulation
9) Calculate Euclidian distance
10) Calculate the total and individual forces, starting with the case where r == 0 to avoid divide by 0 error
11) Calculate for cases where r != 0
12) Calculate acceleration in x and y direction
13) Calculate velocity in x and y direction
14) Calculate updated positions
15) Update loop counter
16) Add results to a dictionary so can be easily printed
17) Loop through identified bodies, printing each result

Known Bugs:
N/A