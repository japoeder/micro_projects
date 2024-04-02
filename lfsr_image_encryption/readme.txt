Name: Jonathan Poeder, JHEDID jpoeder1
Module Info: 
	-Module 8: Object-oriented Programming I
	-Module 8 Assignment: Linear Feedback Shift Registers
	-Due: 10/31/2021 at 11:59 EST

Approach:

LFSR
The approach was basically what's outlined in the assignment - grab
the tap and leftmost bit, do XOR on leftmost bit and tap, remove
leftmost bit, and finally add XOR'ed bit to the right.  I did alter
the tap's parameter from positional to a keyword with default value
of 5 for convenience.

Image Encrypter
Approach here again follows assignment, but basically we're looping
through the image pixels, XOR the LFSR and binary representation of
RGB value to encrypt, update encrypted image object, update LFSR in
current loop with LFSR class built in part 1 of assignment, restart 
loop and repeat until all pixel's RGB values have been encrypted.
Finally, use Pillow to save encrypted image object to disk.

General steps for analysis:

LFSR
1)Set initial password 8bit string (this is the password)
2)Decide the tap position
3)Set the self ‘seed’ and ‘tap’ values from class parameters
4)Create method to return the bit at user supplied tap value (index ‘i’)
5)Execute one LFSR iteration and return new (rightmost) bit as an int
6)Return new bit string that removes leftmost bit and concatenates the 
  new bit from step 5 to the right side.
7)Add calls to invoke LFSR in the main method for testing

Image Encrypter
1) Import your LFSR class for use in ImageEncrypter
2) Initialize an ImageEncrypter object with an LFSR and image file name
3) Set initial values for class parameters
4) Create method to open the image specified by ‘file_name’ in your constructor
5) Create method that calls method from 4 and use Pillow load method to 
	pixelate.  This converts the image to a 2D array of R, G, B triples
6) Create method to encrypt the 2D pixelated “image” returned from pixelate()
	that returns the encrypted 2D array.  Use the binary XOR ('^') operator. To
	do this:
		7) Set RGB value password equal to LFSR, using input bit string
		8) Load he image with method from #5 so you can grab pixels
		9) Get dimension of image from open_image object - going to loop through
			pixel coordinates
		10) Create instance of image object for encryption
		11) Loop through row index first via vertical axis
		12) Loop through column index via horizontal axis
		13) Use x and y coordinates to grab pixel RGB value
		14) Loop through rgb value, encrypt, and update original pixel
		15) Update password
16) Convert the encrypted 2D pixelated image into an image and safe to file

Known Bugs:
N/A

Partner Collaboration:
N/A - I worked alone on this project.