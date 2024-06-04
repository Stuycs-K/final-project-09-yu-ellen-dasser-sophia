import sys
import numpy as np
from encryptWithMatrix import *
from numpy.linalg import inv

def modInv(a, m):
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    raise ValueError(f"No modular inverse for {a} under modulo {m}")

def matrixModInv(matrix, modulus):
    det = int(np.round(np.linalg.det(matrix)))
    detInv = modInv(det % modulus, modulus)
    
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

    # Remove the last number if it corresponds to 'q'
    if decryptedNumbers[-1] == (ord('q') - ord('a')):
        decryptedNumbers.pop()
    
    return numbersToText(decryptedNumbers)

if __name__ == "__main__":
    message, matrix = parseArgs(sys.argv)
    preparedMessage = prepareMessage(message)
    decryptedMessage = decryptMessage(preparedMessage, matrix)
    print(decryptedMessage)








