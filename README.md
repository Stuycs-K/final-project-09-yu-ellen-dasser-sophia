[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-24ddc0f5d75046c5622901739e7c5dd533143b0c8e959d652212380cedb1ea36.svg)](https://classroom.github.com/a/ecp4su41)
# THIS DOCUMENT IS REQUIRED
## Group Info
### Members:
- Ellen Yu
- Sophia Dasser
## Overview

### Historical Context: (1 minutes) Ellen

In 1929, an American mathematician named Lester Hill developed a polygraphic substitution cipher that became known as the Hill Cipher. Lester S. Hill taught mathematics at Princeton, Yale, Hunter College, and the Universities of Maine and Montana. He was also thought to have had a relationship with the military, as he had served in World War 1. In fact, some of his papers were sent to Naval Communications rather than published. This, along with the Hill Cipher, may have helped with encryption and decryption during World War 2. His cipher was the first substitution cipher that allowed operations on groups of more than three characters at a time and marked the beginning of modern mathematical theory and its applications to cryptography. 

### Provide a Background on Matrices and Matrix Multiplication: (3 minutes) Charles Hua and Lisa Li

*[Explain this on a pre-drawn white board with definitions and sudo code matrix multiplication (maybe?):]*

- A matrix can be used as a cipher to encrypt a message. However, the matrix must be invertible for use in decrypting. 
- Matrices that encrypt a message can be thought of as a "key", but instead of calling it a key we'll call it a cipher matrix. To make it easier for us, all our cipher matrix will always be a square matrix with independent column vectors, this will insure that it is always invertable, so we will always be able to decrypt the message.
- Matrix Multiplcation: Show a GIF of matrix multiplication and explain with a few practice problems.
  - Matrix Multiplication will be the way we encrypt our message.
- In order to encrypt plaintext, each character in the plaintext must be denoted with a numerical value and placed into a matrix.
  - These numbers can range in value, but an example is using 1-26 to represent A to Z and 27 to represent a space.
- This matrix is then multiplied with the cipher matrix to form a new matrix containing the ciphertext message.


### Encryption Explained: (3 minutes) Charles Hua and Lisa Li

*[Now show on white board how each letter is a number and how we can multiply the matrices together to encrypt.]*

Each character of the plaintext is given a numerical value as stated before.

These values are then separated into vectors, such that the number of rows of each vector is equivalent to the number of rows of the cipher matrix.
- Values are placed into each vector one at a time, going down a row for each value. Once a vector is filled the next vector is created. If the last vector does not get filled by the plaintext then the remaining entries will hold the value for a space.
- The vectors are then augmented to form a matrix that contains the plaintext.
- The plaintext matrix is then multiplied with the cipher matrix to create the ciphertext matrix.


### Provide a Background on Matrix Inverses: (3 minutes) Sophia Dasser

[write something up]

### Decryption Explained: (2 minutes) Ellen Yu

*[Show on white board how matrix can be inverted and then left multiplied]*

Explain inverses briefly and speak on how a decryption is possible.

- To decrypt a ciphertext matrix the original cipher matrix must be used. The cipher matrix must be inverted in order to
decrypt the ciphertext.
- This inverted cipher matrix is then multiplied with the ciphertext matrix.
- The product produces the original plaintext matrix.
- The plaintext can be found again by taking this product and splitting it back up into its separate vectors, and then converting the numbers back into their letter forms.

### Example of a Hill Cipher Decryption Manually: (2 minutes) Ellen Yu

*[Show on the example on a white board]*

Write out the work for the example

### Example of a Hill Cipher By Code Demo: (2 minutes) Sophia

*[Switch to a terminal and show you running the code]*

```
make encrypt ARGS="plainText fourLetterKey" returns cipherText
make decrypt ARGS="cipherText fourLetterKey" returns plainText
make bruteforce ARGS="cipherText
```

Run this code with any given message and show that we can encrypt and decrypt with a given matrix and message

### More Interesting Things/Futher Applications: (1 minutes) Sophia

If you want to make the encrytption decryptable, you can mod the matrix! Explain how this would work further, and run a new piece of code 

``` 
make hash ARGS="plainText fourLetterKey"
 ```

## Instructions

Files:
encryptWithMatrix.py
decryptWithMatrix.py
hashWithMatrix.py
bruteForce.py
makefile

TryHackMe:
[Hill Cipher](https://tryhackme.com/jr/hillcipher) 

Compilation Steps:

```
make encrypt ARGS="plainText fourLetterKey" // returns cipherText
make decrypt ARGS="cipherText fourLetterKey" // returns plainText
make hash ARGS="plainText fourLetterKey" // returns hashedText

//Note that the following does not work but the logic is there:
make bruteforce ARGS="cipherText" // returns plainText 

```
