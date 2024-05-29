import sys
import numpy as np



def textToNumbers(text):

	numberArray = []

	for char in text:
		numberOfChar = ord(char) - ord('a')
		numberArray.append(numberOfChar)

	return numberArray

def numbersToText(numbers):

	text = ''

	for number in numbers:
		charOfNumber = chr( number +ord('a'))
		text += charOfNumber

	return text


"""
    Encrypt a message using the Hill Cipher with a given 2x2 matrix.

    Args:
        message (str): The plaintext message.
        encryptionMatrix (np.ndarray): The 2x2 encryption matrix.

    Returns:
        The encrypted message (str)
    """

def encryptMessage(message, encryptionMatrix):

	#Given plain text message, convert letters to its index in alphabet

	messageInNumbers = textToNumbers(message)
	encryptedArrayOfVectors = []

	#Split the message into pairs to put in a 2 dimensional vector

	for i in range(0, len(messageInNumbers), 2):
		
		pairVector = np.array(messageInNumbers[i:i+2])

		'''
		Next encrupt the pair by applying matrix multiplication 
		
		Note: dot product and matrix mult. is the same when 
		multplying a vector and a matrix

		'''
		encryptedPair = np.dot(encryptionMatrix,pairVector) % 26

		#Add encrypted par to the new encrypted array of vectors


		# The use of .extend() instead of .append() is necessary adds 
		# each element of an iterable (e.g., list) to the end of the list
		# rather adding its argument as a single element to the end of the list.

		encryptedArrayOfVectors.extend(encryptedPair) 

	return numbersToText(encryptedArrayOfVectors)


# Miscellaneous Functions:


def parseArgs(args):

	if len(args) != 3:
		print("Incorrect number of arguments. Usage: make encrypt ARGS=\"plaintextMessage fourCommaSeperatedValuesForEncryptionMatrix\"")
		sys.exit(1)

	# Parse plaintext message:
	message = args[1]

	# Parse CSV for matrix
	matrixValues = list(map(int, args[2].split(',')))

	if len(matrixValues) != 4:
		print("Encryption matrix must have exactly 4 values.") 
		sys.exit(1)

	# Convert the list of values into a 2x2 matrix

	matrix = np.array(matrixValues).reshape(2, 2)
	return message, matrix

def prepareMessage(message):
	
	# Convert the message to lowercase
	message = message.lower()

	# If the message length is odd, add a padding character (e.g., 'x')
	if len(message) % 2 != 0:
		message += 'x'

	return message


# Main Function:

if __name__ == "__main__":
    message, matrix = parseArgs(sys.argv)
    preparedMessage = prepareMessage(message)
    encrypted_message = encryptMessage(preparedMessage, matrix)
    print(encrypted_message)





