# -*- coding: utf-8 -*-
"""
Created on Wed Sep 15 22:46:26 2021

@author: jonathan
"""

ccNum0 = '520440808656649'
ccNum3 = '461480345960017'

def lhunGenerate(inCC):
    idValue = 0
    # Loop through the string by position number
    for n in range(len(inCC)-1, -1, -1):
        # Set up calculation on just the odd positions
        if n % 2 == 0:
            # Double the number and add to running total if < 10
            if int(inCC[n]) * 2 < 10:
                idValue += int(inCC[n]) * 2
            # Otherwise, just add to running total
            else:
                # Convert the product to a string to parse
                prodStr = str(int(inCC[n]) * 2)
                # Parse string, convert parsed component to an int, then sum
                sumParts = int(prodStr[0]) + int(prodStr[1])
                # Add summed parts to the running total
                idValue += sumParts
        # Now handle the values in even positions        
        else:
            idValue += int(inCC[n])
    
    # Calculate the check digit value
    checkDigit = (10 - (idValue % 10))
    
    return checkDigit

# Run check on CC number 3
#print('')
#print(f'The valid credit card number is: {ccNum0}{lhunGenerate(ccNum0)} \
#and the newly computed check digit is: {lhunGenerate(ccNum0)}')

# Run check on CC number 3
print('')
print(f'The valid credit card number is: {ccNum3}{lhunGenerate(ccNum3)} \
and the newly computed check digit is: {lhunGenerate(ccNum3)}')


