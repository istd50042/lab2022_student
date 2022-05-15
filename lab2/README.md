# Lab 2: Breaking without Brute Force

**Deadline: 29 Sep (2359)**

- [Lab 2: Breaking without Brute Force](#lab-2-breaking-without-brute-force)
  - [Objectives](#objectives)
  - [Introduction](#introduction)
  - [Part I: Substitution Cipher](#part-i-substitution-cipher)
  - [Part II: Compromising OTP Integrity](#part-ii-compromising-otp-integrity)
  - [Submission](#submission)
    - [eDimension Submission](#edimension-submission)

## Objectives

* Break a substitution cipher using frequency analysis and write the decryption function in Python
* Encrypt and decrypt using One-Time Pad (OTP)
* Compromise the integrity of a OTP-encrypted message (if knowing the plain text)

## Introduction

In this lab, you will be sending requests to a remote server [35.197.130.121](http://35.197.130.121/). The server will be up until 1 day after the deadline of 29 Sep (2359).

A Python Client class has already been built for you. See `client.ipynb` or [client_demo.html](client_demo.html) for the usage demonstration for the labs below.

You can use the notebook (`client.ipynb`) or use your own implementation in a Python script for this submission, as long as the outputs are clearly visible for grading purposes.

## Part I: Substitution Cipher

You are provided with a passage that is encrypted with a substition cipher. You only know a few things about it:

1. It is in "normal" English.
2. Spaces (" ") are preserved (the words are intact).
3. Punctuation may not be preserved.
4. It may consist of any characters included the `string.printable` set
5. You will recognise it when it is decrypted correctly.
6. **The verification is not case-sensitive**.

The cipher text is provided in this folder (`story_cipher.txt`), and via a GET request to the endpoint at [http://35.197.130.121/story](http://35.197.130.121/story). You can use `client.get_story_cipher()`. After decrypting, check by posting back to the server with `client.post_story_plaintext()`. 

Questions you can ask yourself:

* Can it be brute forced? (How many possible solutions are there?)
* How can I make use of what I know about the cipher text?

Clues:

* [Wikipedia: Frequency analysis](https://en.wikipedia.org/wiki/Frequency_analysis)
* [Hints for Frequency Analysis](http://www.thiagi.com/instructional-puzzles-original/2015/2/13/cryptograms)
* [The frequency of the letters of the alphabet in English Dictionary](https://www3.nd.edu/~busiforc/handouts/cryptography/letterfrequencies.html)
* [SAS: The frequency of letters in an English corpus](https://blogs.sas.com/content/iml/2014/09/19/frequency-of-letters.html)

Practical hints:

* All the characters in the cipher are upper-case by design to make it easier for you. You can gradually replace them with your hypothesis of the correct lower-case characters and visually inspect the result. You can use Python's `replace` function or any method of your choosing.
* If you are stuck halfway, visually inspect your current cipher, and see if you recognise any words that are only partially decrypted.
* Make sure you keep track of the replacements to ensure you do not "double replace".

In case of server issues: You are provided with `story_cipher.txt` in this folder. Just write a Python script to decrypt it, and submit it together with your decrypted plain text.

## Part II: Compromising OTP Integrity

When you send a POST request to the endpoint at [http://35.197.130.121/score](http://35.197.130.121/score), you will get a cipher text that is unique to your submitted ID (choose anything you like as the ID). You can also ask it to decrypt your cipher text for you.

To get a cipher text, the request body will look something like:

```json
{"request": "get_msg", "id": "100XXXX"}
```

And the response will contain:

```json
{"cipher": "oIiRxZzTB+rHCpOVpnWLctfk8c0J/ylR2Re24nZGSmSJKxOr9635r4PKOrE="}
```

Test that sending back the cipher text gives you a decrypted plain text. Only the server will be able to decrypt your cipher text.

Request:

```json
{"request": "decrypt_msg", "id": "100XXXX",
 "cipher": "oIiRxZzTB+rHCpOVpnWLctfk8c0J/ylR2Re24nZGSmSJKxOr9635r4PKOrE="}
```

Response will contain:

```json
{"plaintext": "Student ID 100XXXX gets a total of 0 points!"}
```

Your aim is to get change the **decrypted plain text response from the server** to say you have gotten **9** points:

```
Student ID 100XXXX gets a total of 9 points!
```

In other words, you manipulate the **cipher text** that you send to the server, so that it decrypts to a plain text of your choosing. Thus, you are compromising the integrity of the encrypted message. 

Note that you need to use `client.base64_decode_bytes()` to decode the response cipher from the server into a Python `bytearray`. Likewise, use `client.base64_encode_bytes()` to encode the cipher before sending it to the server. You can refer to `client.ipynb` or [client_demo.html](client_demo.html) for example usage.

Hints:

* The ciphertext is encrypted with a OTP. You do not know what the OTP is, you also cannot crack it. However, the server will remember the OTP, since it requires it to decrypt the message. You can ask the server to decrypt your message any time. 
* **You do not need to know anything about the OTP for this exercise.**
* (If the server restarts, the OTP is reset. Don't hardcode your cipher text in your submission - request for it each time your code runs.)

In case of server issues: You are provided with `ex2.backup.py` in this folder. It contains the same exercise: make the cipher text decrypt to a message of your choosing, without knowing the randomly generated OTP key.

## Submission

### eDimension Submission

Submission ground rules:

* Please make sure to indicate your name and student ID in each of the graded submission files
* You are allowed to collaborate with **one** other student. If you choose to do so, both of your name/student ID should be indicated in the submission files. Both are still required to submit the files individually. 
* Except for within each pair of students that are collaborating, you are not allowed to share answers and solutions.

Lab 2 submission:

Upload a **zip file** with the following:

Option 1:

* `client.ipynb` (with the outputs saved, and any code needed to perform the decryption etc)
* **Clear all outputs and run the entire notebook before submitting.**

OR

Option 2 (**mainly in case of server issues**):

* `ex1.py`, your python script to perform decryption of the substitution cipher (`story_cipher.txt`)
* Decrypted plain text for Part I as `solution.txt`
* `ex2.py`, your python script to change the OTP message, you can based it on `ex2.backup.py`

**For both options: you will not get the grade if your submission is not runnable.**

**Deadline: 29 Sep (2359)**
