import sys
import numpy as np
from encryptWithMatrix import *



def hashWithMatrix(plainText, key):
    keyMatrix = createMatrixFromKey(key)
    textVector = [ord(char) - ord('a') for char in plainText]
    hashedText = ''

    # Perform hashing by taking each pair of characters and applying the key matrix
    for i in range(0, len(textVector), 2):
        vector = np.array(textVector[i:i+2]).reshape(2, 1)
        hashedVector = np.mod(vector, keyMatrix)
        hashedText += chr(hashedVector[0, 0] + ord('a'))
        hashedText += chr(hashedVector[1, 0] + ord('a'))

    return hashedText

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: make hash ARGS=\"plainText key\"")
        sys.exit(1)

    plainText = sys.argv[1]
    key = sys.argv[2]

    if len(key) != 4:
        print("Key must be 4 characters long.")
        sys.exit(1)

    hashedText = hashWithMatrix(plainText, key)
    print(f"Hashed Text: {hashedText}")


'''
Explanation of this code:

This code essentially creates a hash version of the Hill Cipher, 
but instead of encrypting the text, it uses the key matrix to modify 
the indices of each character through modular linear algebra.

Here's the psuedo code:
1. Create the key matrix from the given 4 character key
2. Convert the input text into pair vectors
3. For each pair you'll apply the key matrix using modulus operation
instead of matrix multiplication
4. Combine the resulting characters into a hashed string

This allows us to effectivley create a non-reversible hash because the 
operation performed doesn't rely on the invertibility of the matrix but 
rather the invertibility of the modulus operation.

'''