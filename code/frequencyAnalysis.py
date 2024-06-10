import string
import sys

def fileToString(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            file_content = file.read()
        return file_content
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return None
    except Exception as e:
        print(f"Error reading file '{filename}': {e}")
        return None

def frequencyCalc (text):
	# Initialize list of frequencies for each letter
	frequenciesList = [0] * 26

	# Letter Counter, will eventually be our denominator for frequency
	letterCount = 0

	# Open File:

	for char in text:
		# According to google this is a good idea to include to ensure that you are only showing letter frequency and not spaces/other punctuation.
		if char.isalpha(): 
			if (65 <= ord(char) and ord(char) <= 90) or (97 <= ord(char) and ord(char) <= 122):
				letterCount += 1
				char = char.lower()
				index = ord(char) - ord('a')
				#if index > 25 or index < 0:
					#print(char)
					#print(index)
				frequenciesList[index] += 1

	for i in range(len(frequenciesList)):
		frequenciesList[i] = frequenciesList[i] / letterCount

	return frequenciesList

def printFreq(frequenciesList):

	index = 0
	for freq in frequenciesList:  # Use enumerate to get both index and value
		print(chr(ord('A') + index),":", round(freq, 5)) # Fix the format string
		index += 1

if __name__ == "__main__":

    # Check if the correct number of command-line arguments is provided
    if len(sys.argv) != 2:
        print("Usage: python frequencyAnalysis.py <inputFileName>")
        sys.exit(1)

    # Get the input filename from the command-line arguments
    fileName = sys.argv[1]
    # Calculate letter frequencies for the specified file
    frequencies = frequencyCalc(fileToString(fileName))
    # Print the letter frequencies
    printFreq(frequencies)







    


