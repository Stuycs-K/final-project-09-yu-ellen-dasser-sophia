[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-24ddc0f5d75046c5622901739e7c5dd533143b0c8e959d652212380cedb1ea36.svg)](https://classroom.github.com/a/ecp4su41)
# Hill Cipher Project

## Group Info
### Members:
- Ellen Yu
- Sophia Dasser

## Project Description:

This project implement the Hill Cipher, a polygraphic substitution cipher invented by Lester S. Hill in 1929. The Hill cipher was the first cipher to utilize linear algebraic techniques and matrix multiplication for encryption and decryption. This project includes scripts for encrypting and decrypting messages using the Hill cipher, as well as brute-forcing decryption using frequency analysis.


## Directions

### Prerequisites
Ensure you have Python and `numpy` installed. You can install `numpy` using `pip`:

```
pip install numpy
```

### Files:
* encryptWithMatrix.py: Script to encrypt plaintext using the Hill cipher.
* decryptWithMatrix.py: Script to decrypt ciphertext using the Hill cipher.
* hashWithMatrix.py: Script to create a non-reversible hash using the Hill cipher.
* bruteForceDecrypt.py: Script to brute-force decrypt a ciphertext using frequency analysis.
* makefile
* frequencyAnalysis.py: Helper script for frequency analysis.
* frequencyDistance.py: Helper script for calculating frequency distances.
* alice.txt: Sample text file used for frequency analysis.

### TryHackMe Resource/Homework:
[Hill Cipher](https://tryhackme.com/jr/hillcipher) 

### Compilation Steps:

```
make encrypt ARGS="plainText fourLetterKey" # returns cipherText
make decrypt ARGS="cipherText fourLetterKey" # returns plainText
make hash ARGS="plainText fourLetterKey" # returns hashedText

# Note that the following does *not* work but the logic is in the comments:
make bruteforce ARGS="cipherText" # returns plainText 

```

### Presentation Video and Documentation
* [Presentation Video](google.com) 
* [Presentation Slides](https://drive.google.com/file/d/1zyEIDTR-1Yvs42OJqPmAcmtStb4c8B05/view?usp=sharing)
* [Presentation Outline](https://drive.google.com/file/d/1Zs2RpToGa_eoJB-ugvRAU3V7CHzgLuqx/view?usp=sharing)

