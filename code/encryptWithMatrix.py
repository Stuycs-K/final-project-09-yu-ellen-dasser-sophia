import sys
import numpy as np

def createMatrixFromKey(key):
    keyMatrix = [[ord(key[0]) - ord('a'), ord(key[1]) - ord('a')],
                 [ord(key[2]) - ord('a'), ord(key[3]) - ord('a')]]
    return np.array(keyMatrix)


def encryptMessage(plainText, key):
    keyMatrix = createMatrixFromKey(key)
    print(keyMatrix)
    textVector = [ord(char) - ord('a') for char in plainText]
    if len(textVector) % 2 != 0:
        textVector.append(ord('x') - ord('a'))  # Padding if plaintext length is odd

    encryptedText = ''
    for i in range(0, len(textVector), 2):
        vector = np.array(textVector[i:i+2]).reshape(2, 1)
        encryptedVector = np.dot(keyMatrix, vector) % 26
        encryptedText += chr(encryptedVector[0, 0] + ord('a'))
        encryptedText += chr(encryptedVector[1, 0] + ord('a'))

    return encryptedText


if __name__ == "__main__":

    if len(sys.argv) != 3:
        print("Usage: make encrypt ARGS=\"plaintext key\"")
        sys.exit(1)

    plainText = sys.argv[1]
    key = sys.argv[2]

    if len(key) != 4:
        print("Key must be 4 characters long.")
        sys.exit(1)

    cipherText = encryptMessage(plainText, key)
    print(f"Encrypted Text: {cipherText}")
