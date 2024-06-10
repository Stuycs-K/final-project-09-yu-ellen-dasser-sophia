import sys
import itertools
import frequencyAnalysis
import frequencyDistance
from encryptWithMatrix import *
from decryptWithMatrix import * 
import numpy as np

def decrypt(cipherText, key):
    keyMatrix = createMatrixFromKey(key)
    if not isMatrixInvertible(keyMatrix):
        return None  # If matrix is not invertible, return None

    determinant = int(np.round(np.linalg.det(keyMatrix))) % 26
    inverseDet = modInverse(determinant, 26)
    adjugateMatrix = np.array([[keyMatrix[1, 1], -keyMatrix[0, 1]], [-keyMatrix[1, 0], keyMatrix[0, 0]]])
    inverseKeyMatrix = (inverseDet * adjugateMatrix) % 26

    textVector = [ord(char) - ord('a') for char in cipherText]
    decryptedText = ''

    for i in range(0, len(textVector), 2):
        vector = np.array(textVector[i:i+2]).reshape(2, 1)
        decryptedVector = np.dot(inverseKeyMatrix, vector) % 26
        decryptedText += chr(decryptedVector[0, 0] + ord('a'))
        decryptedText += chr(decryptedVector[1, 0] + ord('a'))

    return decryptedText

def bruteForceDecrypt(cipherText):
    possibleKeys = itertools.product('abcdefghijklmnopqrstuvwxyz', repeat=4)
    standardFrequencies = frequencyAnalysis.frequencyCalc(frequencyAnalysis.fileToString("alice.txt"))
    bestGuess = cipherText
    bestDistance = frequencyDistance.frequencyDistance(frequencyAnalysis.frequencyCalc(cipherText), standardFrequencies)

    for keyTuple in possibleKeys:
        key = ''.join(keyTuple)
        decryptedText = decrypt(cipherText, key)
        if decryptedText is None:
            continue

        currentDistance = frequencyDistance.frequencyDistance(frequencyAnalysis.frequencyCalc(decryptedText), standardFrequencies)
        if currentDistance < bestDistance:
            bestDistance = currentDistance
            bestGuess = decryptedText

    return bestGuess

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: make bruteforce ARGS=\"ciphertext\"")
        sys.exit(1)

    cipherText = sys.argv[1]
    plainText = bruteForceDecrypt(cipherText)
    print(f"Decrypted Text: {plainText}")


'''
Explanation of this code:

This code essentially brute forces a given ciphertext by doing the following logic:
1. Generate all possible 4-character keys (26^4 combinations) which can form 2x2 matrices.

2. For each possible key:
   a. Create a key matrix from the key.
   b. Check if the key matrix is invertible (necessary for decryption). Fun fact: this takes out a lot of matrices
   c. If the matrix is invertible, use it to decrypt the ciphertext.
   d. Perform frequency analysis on the decrypted text.
   e. Calculate the frequency distance between the decrypted text and expected letter frequencies in English.
   f. Store the decrypted text with the smallest frequency distance as the best guess.

3. Return the best guess for the decrypted text.

'''