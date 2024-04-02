Name: Jonathan Poeder, JHEDID jpoeder1
Module Info: 
	-Module 7: Midterm
	-Module 7 Assignment: Frequency Analysis
	-Due: 10/17/2021 at 11:59 EST

Approach:

Import text string and frequency counts, creating a dict
for frequencies.  Then generate frequencies for letters
in the ciphertext in get_freq_counts().  Compare ciphertext 
frequencies with the ones provided in the frequency text 
file, manually correcting decrypted message per the instructions.
Then build process to match and build deciphered string in the 
get_freq_counts() function.  

To reduce the error I tested a number of strategies including
applying the weights detailed on the Cornell site, but
unfortunately this didn't seem to help.  I would have preferred
to use a random number generator from a uniform distribution in
the weighting calculation, as I think this could have helped.
For this I'd use numpy / random, but we're instructed to not 
import libraries for deciphering and calculating the frequencies.

I assumed that using 'hashlib' would be acceptable since I'm
just using to validate the md5 of the manually corrected string.
Note that I also generated an md5 with the website provided, and
it too yielded the correct value.

General steps for analysis:

1) Import hashlib to check MD5 later
2) Set path for text files
3) Instantiate a string object for md5
4) Read in the cypher text
5) Read in the frequency data
6) Parse lines of data
7) First row is parsed differently for space character
8) Now parse other regular characters
9) Create a dict for frequencies
10) Loop through characters in cipher
11) If the loop letter value is in the dictionary, do the following:
	12) Increment count by 1
	13) Otherwise, insert it into the dictionary with a count of 1
14) Sort the dictionary for easier comparison
15) Grab the ciphertext frequency from frequency dict for the loop letter.
16) Next, get a list of letters with same frequency
17) If the index of the cipher letter is even, sort asc
18) Else sort desc (17 & 18 help mix up selection to help reduce misassignment)
19) Set a break point for while loop once a deciphered letter is selected (dealing with multiple that have same freq)
20) Create a counter for list index
21) Next, loop through possible characters from decipher list.
22) Grab loop letter from decrypted letter option list
23) See if there are any left in temp count decipher list
24) Set break value for outer loop since there are some left
25) Add selected deciphered letter to string
26) If there are still some to allocate from freq dict, decrement and add to decryption string
27) Otherwise, add to decryption string and drop from temp freq dict
28) Now decrement from temp cipher letter count dict
29) Otherwise, delete if none left
30) If loop letter exhausted from temp count of decipher letters, check next in list
31) Print the final deciphered message
32) Kick off frequency count function
33) Correct text where needed
34) Generate md5 and compare to provided value
35) Print output

Known Bugs:
N/A