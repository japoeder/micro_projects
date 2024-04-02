Name: Jonathan Poeder, JHEDID jpoeder1
Module Info: 
	-Module 11: Data Science I
	-Module 11 Assignment: Hill Cipher
	-Due: 11/14/2021 at 11:59 EST
	
Approach:
Follow instructions outlined in the assignment as described in the general steps below.  Note that I have attempted to make the code dynamic such that it can accept a key and converted plaintext matrix with greater than the prescribed dimensionality.


General Steps:

1) Initialize a HilLCypher object with a key and plaintext string
2) Create translation dicts for alpha to num and num to alpha conversions
3) Grab the dimensions of the key matrix
4) Check to see if string is evenly divisible by key matrix column count.  This is because we need the key matrix columns to match the row count for the resulting matrix we create from the plaintext string.
5) If not, throw error that dimensions don't match
6) Next, determine / calculate the dimensions of the resultant plaintext matrix
7) Create an array list, and parse plaintext into a list
8) Use list comprehension to break the string into groups that we'll reshape to column vectors next
9) Convert list to array and reshape
10) Build method for converting numpy arrays to text by grabing the dimensions of the key matrix
12) Grab the dimensions of the input array
12) Convert array to list of reshaped lists
13) Flatten list of lists to single list
14) Convert flattened list to encrypted string
15) Build method to calculate determinant.
16) If the matrix is square, calculate the determinant, if not raise error.
17) After calculating the determinant, if it's 0 raise error.
18) If the determinant can be calc'd and isn't 0, return value.
19) Calculate the modular multiplicative inverse.
20) Note that we'll to use abs value of determinant.
21) Check invertibility.
22) Convert string to list of array.
23) Process each column vector
24) Grab the encrypted string
25) Print some values
26) Grab the determinant and modular inverse
27) Calculate the modular multiplicative inverse of our key matrix
28) Start with the inverse of the key matrix
29) Multiply by determinant and modular inverse
30) Grab columns of from first part of mmi
31) Create identity matrix of same size and flip
32) Multiply flipped identity matrix by mod and add to mmi to complete the calculation
33) Convert string to list of array
34) Process each column vector
35) Print some values


Known Bugs:
The code is able to produce the output of the assignment, but I haven't tested the performance with keys greater than 2 x 2 or longer plaintext strings.  There could be bugs associated with this functionality.