# Import hashlib to check MD5 later
import hashlib

# Set path for text files
myPath = "C:/Users/japoe/Documents/schoolData/"

# Instantiate a string object for md5
md5Hash = 'c674b76e1ada393c4274ada8490a888d'

# Read in the cypher text
cFile = open(myPath + 'ciphertext.txt', 'r')
cText = cFile.readlines()[0]

# Read in the frequency data
frFile = open(myPath + 'freq.txt', 'r')
frequencies = frFile.readlines()
frDict = {}

# Parse lines of data
for i, f in enumerate(frequencies):

    # First row is parsed differently for space character
    if i == 0:
        frDict[' '] = int(f.strip().split(':')[1])
    # Now parse other regular characters
    else:
        frDict[f.strip().split(':')[0]] = int(f.strip().split(':')[1])


def get_freq_counts(c_in):
    # Create a dict for frequencies
    cipher_char_ct = {}
    for c in c_in:  # Loop through characters in cipher
        if c in cipher_char_ct:  # If the loop letter value is in the dictionary, do the following:
            cipher_char_ct[c] += 1  # Increment count by 1
        else:
            cipher_char_ct[c] = 1  # Otherwise, insert it into the dictionary with a count of 1

    # Sort the dictionary for easier comparison
    cccSorted = dict(sorted(cipher_char_ct.items(), key=lambda item: item[1], reverse=True))
    cccSorted2 = dict(sorted(cipher_char_ct.items()))
    cccSorted_temp = cccSorted.copy()
    frDict_temp = frDict.copy()

    dec_c_in = ''
    for c in c_in:

        # Grab the ciphertext frequency from frDict for the loop letter.
        F = cccSorted[c]

        # Next, get a list of letters with same frequency
        lOpt_pre = [key for (key, value) in frDict.items() if value == F]

        # If the index of the cipher letter is even, sort asc
        if c_in.index(c) % 2 == 0:
            lOpt = sorted(lOpt_pre)
        # Else sort desc
        else:
            lOpt = sorted(lOpt_pre, reverse=True)

        # Set a break point for while loop once a deciphered letter is selected
        loop_break = 0

        # Create a counter for list index
        L = 0

        # Next, loop through possible characters from decipher list.
        while loop_break == 0:

            # Grab loop letter from decrypted letter option list
            loop_letter = lOpt[L]

            # See if there are any left in temp count decipher list
            if loop_letter in frDict_temp:

                # Set break value for outer loop since there are some left
                loop_break = 1

                # Add selected deciphered letter to string
                dec_c_in = dec_c_in + loop_letter

                # If there are still some to allocate from freq dict, decrement and add to decryption string
                if frDict_temp[loop_letter] != 1:
                    frDict_temp[loop_letter] -= 1

                # Otherwise, add to decryption string and drop from temp freq dict
                else:
                    del frDict_temp[loop_letter]

                # Now decrement from temp cipher letter count dict
                if cccSorted_temp[c] != 1:
                    cccSorted_temp[c] -= 1

                # Otherwise, delete if none left
                else:
                    del cccSorted_temp[c]

            # If loop letter exhausted from temp count of decipher letters, check next in list
            else:
                L += 1

    # Print the final deciphered message
    print()
    print('Deciphered message is:')
    print(dec_c_in[0:54])
    print(dec_c_in[54:104])
    print(dec_c_in[104:153])
    print(dec_c_in[153:])
    print()

    return dec_c_in


# Kick of frequency count function
cCount = get_freq_counts(cText)

# Deciphered and corrected text string is as follows
dText = 'ltcol thorn are the oss agents meeting in the rear of saint marys south church after rear admiral smith returns from his travel abroad to mauritania for operation illicitscent'
print('Corrected output text is:')
print(dText[0:54])
print(dText[54:104])
print(dText[104:153])
print(dText[153:])
print()
print('Provided MD5 is:')
print(md5Hash)
print()
print('Deciphered & corrected MD5 is:')
dMD5 = hashlib.md5(dText.encode()).hexdigest()
print(dMD5)
