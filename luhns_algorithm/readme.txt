Name: Jonathan Poeder, JHEDID jpoeder1
Module Info: 
	-Module 3: Control Structures and Conditional Statements
	-Module 3 Assignment: Credit Card Checksum
	-Due: 09/19/2021 at 11:59 EST
Approach:

I chose to define a function so I'd be able to simply provide 
any new number to the function and have it either validate 
the number or provide the correct final digit (depending on the
function executed). The steps for each program are broken out 
below.  After defining the function it is called by the print
statements, producing the required text in the output
window.

PART 1:
1) Loop through the string by position number
2) Set up calculation on just the odd positions
	3) Double the number and add to running total if < 10
	4) If the number is > 10, convert the product to a string to parse
	5) Parse string, convert parsed components to int, then sum
	6) Add summed parts to the running total
7) Now handle the values in even positions, add directly to running total
8) Calculate the checksum
9) Set the string for valid and invalid CC nums
10) Return a list of key results
11) Run check on CC number 1
12) Run check on CC number 2

PART 2:
1) Loop through the string by position number
2) Set up calculation on just the odd positions
	3) Double the number and add to running total if < 10
	4) If the number is > 10, convert the product to a string to parse
	5) Parse string, convert parsed components to int, then sum
	6) Add summed parts to the running total
7) Now handle the values in even positions, add directly to running total 
8) Calculate and return the check digit number
9) Run check on CC number 3

Known Bugs:
N/A