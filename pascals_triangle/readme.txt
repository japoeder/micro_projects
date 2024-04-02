Name: Jonathan Poeder, JHEDID jpoeder1
Module Info: 
	-Module 6: Functions
	-Module 6 Assignment: Pascal's Triangle
	-Due: 10/10/2021 at 11:59 EST
Approach:

I designed a function as prescribed by the assignment
so that the calculations can be run on any number of
values for catalan / pascal.  Catalan is pretty straight-
forward and just need to understand the product (pi)
piece for the most part.  Pascal triangle is trickier
with the recursion, but just need to understand how Python
compiles and unpacks in execution.  Essentially, for a given
loop, you need information from the last iteration to
generate results for current one.

General Steps for Catalan:

1) Create the main method
2) Start with 4 sided p-gon and loop through 17 sided to get order 15
3) Return NoneType
4) Start catalan function by asking for new input if p < 4
5) Set initial catalan output to 1 for factorial calc
6) Set n from formulae to initial value of p - 2
7) Loop through k from formulae, from 2 to n as specified by formula range
8) Calculate the ratio value for the loop
9) Use '*=' to represent the product notation pi
10) Print results from the catalan function
11) Press the green button in the gutter to run the script.

General Steps for Pascal:

1) Create the main method
2) Call the pascal function, and generate first 10 rows
3) When n hits 0, recursion returns nothing
4) Instantiate a new list at each iteration with 1 as the first element in the new row
5) Going to skip calcs for first row explicitly and second row implicitly via pascal(2-1) => pascal(1)
6) Grab results from last iteration
7) Loop through the prior row / list so new row can be calculated
8) Add 1 to the right side of the new list
9) Print without the brackets and delimit with a space
10) Press the green button in the gutter to run the script.

Known Bugs:
N/A