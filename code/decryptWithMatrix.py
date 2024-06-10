import sys
import numpy as np
from encryptWithMatrix import *

def modInv(a, m):
    a = a % m
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    raise ValueError(f"No modular inverse for {a} under modulo {m}")

def matrixModInv(matrix, modulus):
    det = int(np.round(np.linalg.det(matrix)))
    det = det % modulus
    try:
        detInv = modInv(det, modulus)
    except ValueError as e:
        raise ValueError(f"Matrix determinant {det} has no modular inverse under modulo {modulus}.") from e
    adjugate = np.array([[matrix[1,1], -matrix[0,1]], 
                         [-matrix[1,0], matrix[0,0]]])
    matrixInv = (detInv * adjugate) % modulus
    return matrixInv

def decryptMessage(message, encryptionMatrix):
    messageNumbers = textToNumbers(message)
    decryptedNumbers = []
    decryptionMatrix = matrixModInv(encryptionMatrix, 26)
    for i in range(0, len(messageNumbers), 2):
        pair = np.array(messageNumbers[i:i+2])
        decryptedPair = np.dot(decryptionMatrix, pair) % 26
        decryptedPair = decryptedPair.astype(int)
        decryptedNumbers.extend(decryptedPair)
    if decryptedNumbers[-1] == (ord('q') - ord('a')):
        decryptedNumbers.pop()
    return numbersToText(decryptedNumbers)

def parseArgs(args):
    if len(args) != 3:
        print("Incorrect number of arguments. Usage: make decrypt ARGS=\"ciphertextMessage 4letterKey\"")
        sys.exit(1)
    message = args[1]
    key = args[2]
    return message, key

if __name__ == "__main__":
    message, key = parseArgs(sys.argv)
    preparedMessage = prepareMessage(message)
    matrix = createMatrixFromKey(key)
    decryptedMessage = decryptMessage(preparedMessage, matrix)
    print(decryptedMessage)
