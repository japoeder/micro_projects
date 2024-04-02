# -*- coding: utf-8 -*-
"""
Created on Wed Sep 15 22:46:26 2021

@author: jonathan
"""

ccNum0 = '5204408086566492'
ccNum1 = '3379513561108795'
ccNum2 = '4614803459600172'

def lhunVerify(inCC):
    idValue = 0
    # Loop through the string by position number
    for n in range(len(inCC)):
        # Set up calculation on just the odd positions
        if n % 2 == 0:
            # Double the number and add to running total if < 10
            if int(inCC[n]) * 2 < 10:
                idValue += int(inCC[n]) * 2
            # Otherwise, add digits and add to running total
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
    
    # Calculate the checksum
    checkSum = idValue % 10
    
    # Set the string for valid and invalid CC nums
    if checkSum == 0:
        verStat = 'a valid'
    else:
        verStat = 'an invalid'
    
    # We're going to return a list of key results
    return [verStat, checkSum, idValue]

# Run check on CC number 0
#print('')
#print(f'Checksum = {lhunVerify(ccNum0)[1]}')
#print(f'idValue = {lhunVerify(ccNum0)[2]}')
#print(f'{ccNum0} {lhunVerify(ccNum0)[0]} CC number.')

# Run check on CC number 1
print('')
print(f'Checksum = {lhunVerify(ccNum1)[1]}')
#print(f'idValue = {lhunVerify(ccNum1)[2]}')
print(f'{ccNum1} {lhunVerify(ccNum1)[0]} CC number.')

# Run check on CC number 2
print('')
print(f'Checksum = {lhunVerify(ccNum2)[1]}')
#print(f'idValue = {lhunVerify(ccNum2)[2]}')
print(f'{ccNum2} {lhunVerify(ccNum2)[0]} CC number.')




