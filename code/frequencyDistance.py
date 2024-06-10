import string
import sys
import math
import frequencyAnalysis

def frequencyDistance (frequenciesTableA, frequenciesTableB):

	sumOfSquares = 0
	for i in range(len(frequenciesTableA)):
		sumOfSquares += pow(frequenciesTableB[i] - frequenciesTableA[i], 2)

	return math.sqrt(sumOfSquares)



if __name__ == "__main__":

    # Check if the correct number of command-line arguments is provided
    if len(sys.argv) != 3:
        print("Usage: python frequencyDistance <inputFileNameA> <inputFileNameB>")
        sys.exit(1)

    # Get the input filename from the command-line arguments
    fileA = sys.argv[1]
    # print(fileA)
    fileB = sys.argv[2]
    # print(fileB)


    # Calculate letter frequencies for the specified file
    frequenciesA = frequencyAnalysis.frequencyCalc(frequencyAnalysis.fileToString(fileA))
    frequenciesB = frequencyAnalysis.frequencyCalc(frequencyAnalysis.fileToString(fileB))
    
    result = frequencyDistance(frequenciesA, frequenciesB)

    # Displaying the result with a large number of decimal places
    print(result)