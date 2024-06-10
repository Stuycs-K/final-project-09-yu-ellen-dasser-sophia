import sys
import numpy as np
from encryptWithMatrix import *

def modInverse(a, m):
    a = a % m
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return None

def isMatrixInvertible(matrix):
    determinant = int(np.round(np.linalg.det(matrix))) % 26
    return determinant != 0 and modInverse(determinant, 26) is not None


def decryptMessage(cipherText, key):
    keyMatrix = createMatrixFromKey(key)
    if not isMatrixInvertible(keyMatrix):
        print("Error: Key matrix is not invertible.")
        sys.exit(1)

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


if __name__ == "__main__":

    if len(sys.argv) != 3:
        print("Usage: make decrypt ARGS=\"ciphertext key\"")
        sys.exit(1)

    cipherText = sys.argv[1]
    key = sys.argv[2]

    if len(key) != 4:
        print("Key must be 4 characters long.")
        sys.exit(1)

    plainText = decryptMessage(cipherText, key)
    print(f"Decrypted Text: {plainText}")
